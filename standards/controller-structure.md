# Jails Controller Structure and Function Ordering

## Controller Structure Convention

Jails controller files must follow a consistent structure to ensure readability and maintainability. This document defines the standard ordering for all parts of a Jails controller.

## Canonical Ordering

Every Jails controller must follow this order:

```typescript
// 1. IMPORTS
import type { Component } from 'jails-js'
import { cancelable } from 'jails.stdlib/cancelable'
import { someService } from '../../services/example'
import { appStore } from '../../store/app'
import type { LocalState } from './types'

// 2. EXPORT DEFAULT FUNCTION
export default function componentName({
	main,
	on,
	state,
	unmount,
}: Component) {
	// 2a. CLOSURE VARIABLES (let, var)
	let unsubscribe: (() => void) | undefined

	// 2b. ASYNC/HELPER FUNCTIONS (const with async or cancelable)
	const fetchData = cancelable(async () => {
		// Implementation
	})

	// 2c. MAIN CALLBACK
	main(() => {
		on('submit', 'form', handleSubmit)
		updateState(appStore.getState())
		unsubscribe = appStore.subscribe(updateState)
		fetchData()
	})

	// 2d. UNMOUNT CALLBACK
	unmount(() => {
		unsubscribe?.()
		// cancelable auto-cleanup
	})

	// 2e. HELPER/EVENT HANDLER FUNCTIONS (arrow functions)
	const updateState = (snapshot: State) => {
		state.set({ /* ... */ })
	}

	const handleSubmit = async (event: Event) => {
		// Implementation
	}
}

// 3. EXPORTS (model and view)
export const model: ComponentModel = { /* ... */ }
export const view = (state: ComponentModel) => ({ /* ... */ })
```

## Detailed Sections

### 1. Imports
All imports at the top of the file:
- Framework imports (`jails-js`, `jails-stdlib/*`)
- Domain services, constants
- Store imports
- Local type imports

```typescript
import type { Component } from 'jails-js'
import { cancelable } from 'jails.stdlib/cancelable'
import { getWeatherForecast } from '../../services/open-meteo'
import { weatherStore } from '../../store/weather'
import type { WeatherState } from '../../store/types'
import type { LocalComponentModel } from './types'
```

### 2a. Closure Variables
Declare mutable variables that will be accessed in multiple functions:

```typescript
let unsubscribe: (() => void) | undefined
```

These variables capture state that persists across the component's lifecycle.

### 2b. Async/Cancelable Functions
Declare async functions or functions wrapped with `cancelable`:

```typescript
const fetchData = cancelable(async (query: string) => {
	try {
		const result = await service.fetch({ query })
		await appStore.dispatch(appStore.Actions.setData, { result })
	} catch (error) {
		// Handle error
	}
})
```

**Key point:** These functions are declared before `main()` because they're referenced inside `main()`.

### 2c. Main Callback
The initialization callback:

```typescript
main(() => {
	on('click', 'button', handleClick)
	updateState(appStore.getState())
	unsubscribe = appStore.subscribe(updateState)
	fetchData()
})
```

**Rules inside main():**
- Register event handlers with `on()`
- Initialize component state
- Set up subscriptions
- Call async initialization functions
- **No branching or new declarations**

### 2d. Unmount Callback
Resource cleanup:

```typescript
unmount(() => {
	unsubscribe?.()
	// cancelable auto-cleanup of pending requests
})
```

### 2e. Helper and Event Handler Functions
All arrow functions that handle events or transform state:

```typescript
const updateState = (snapshot: State) => {
	state.set({ /* ... */ })
}

const handleClick = async (event: Event) => {
	// Handler implementation
}

const handleSubmit = (event: Event) => {
	event.preventDefault()
	// Handler implementation
}
```

These functions are declared **after** `main()` and `unmount()`. They reference values from closure and are called from `main()`.

### 3. Exports
Final exports at the end of the file:

```typescript
export const model: ComponentModel = {
	isLoading: false,
	data: null,
}

export const view = (state: ComponentModel): ComponentView => ({
	...state,
	computedProperty: state.isLoading ? 'loading' : 'ready',
})
```

## Why This Order?

### Readability
The structure follows the **narrative flow** of the component:
1. What we import (dependencies)
2. How the component initializes (main)
3. How it cleans up (unmount)
4. How it handles interactions (helpers after cleanup)
5. What state it exports (model/view)

### Prevents Forward References
By declaring async functions before `main()` and helpers after, we avoid forward reference issues:
- `fetchData` can be called in `main()`
- `updateState` can be called in `main()` and `fetchData`

### Consistency
Every component uses the same structure, making it easy to scan and understand any controller.

### Jails Conventions
This follows the upstream Jails component conventions: functions are defined once and in a logical sequence, with no branching inside callbacks.

## Example: Complete Component

```typescript
import type { Component } from 'jails-js'
import { cancelable } from 'jails.stdlib/cancelable'
import { searchLocation } from '../../services/geocoding'
import { weatherStore } from '../../store/weather'
import type { WeatherStoreState } from '../../store/types'
import type { SearchModel } from './types'

export default function weatherSearch({
	main,
	on,
	state,
	unmount,
}: Component) {
	// CLOSURE VARIABLES
	let unsubscribe: (() => void) | undefined

	// ASYNC/HELPER FUNCTIONS
	const performSearch = cancelable(async (query: string) => {
		state.set({ isSearching: true })

		try {
			const { location } = await searchLocation({ query })

			if (!location) {
				state.set({ error: 'Location not found' })
				return
			}

			await weatherStore.dispatch(weatherStore.Actions.setLocation, { location })
		} catch (error) {
			const message = error instanceof Error ? error.message : 'Search failed'
			state.set({ error: message })
		} finally {
			state.set({ isSearching: false })
		}
	})

	// MAIN CALLBACK
	main(() => {
		on('submit', 'form', handleSubmit)
		updateSearch(weatherStore.getState())
		unsubscribe = weatherStore.subscribe(updateSearch)
	})

	// UNMOUNT CALLBACK
	unmount(() => {
		unsubscribe?.()
	})

	// HELPER FUNCTIONS
	const updateSearch = (snapshot: WeatherStoreState) => {
		state.set({
			hasLocation: snapshot.selectedLocation !== null,
			searchStatus: snapshot.searchStatus,
		})
	}

	const handleSubmit = async (event: Event) => {
		event.preventDefault()

		if (!(event.target instanceof HTMLFormElement)) return

		const form = event.target
		const formData = new FormData(form)
		const query = formData.get('query') as string

		if (query.length < 2) {
			state.set({ error: 'Query too short' })
			return
		}

		await performSearch(query)
	}
}

// EXPORTS
export const model: SearchModel = {
	hasLocation: false,
	isSearching: false,
	error: '',
}

export const view = (state: SearchModel) => ({
	...state,
	formClass: state.hasLocation ? 'mt-4' : 'mt-12',
})
```

## Verification Checklist

Before delivery, verify:

- ✅ Imports organized by category
- ✅ Closure variables declared before functions
- ✅ Async/cancelable functions before `main()`
- ✅ `main()` callback with no branching
- ✅ `unmount()` callback with cleanup
- ✅ All helpers/handlers after `unmount()`
- ✅ Model and view exports at end of file
- ✅ No forward references or circular dependencies
- ✅ No declarations or branching inside `main()` or `unmount()`
- ✅ All functions follow naming conventions

This structure ensures predictable, maintainable controller code across all jails-ai projects.
