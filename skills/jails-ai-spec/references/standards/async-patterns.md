# Async patterns with jails.stdlib

## Cancelable requests

When a component needs to perform asynchronous operations (such as API calls), use the `cancelable` function from `jails.stdlib/cancelable` to automatically handle request cancellation when:

- The user triggers a new request before the previous one completes
- The component unmounts while a request is pending

This prevents:
- Race conditions where stale responses update state after a newer request
- Memory leaks from incomplete promises after unmount
- Unnecessary state updates on unmounted components

### Pattern: Async form submission with cancelable

```typescript
import type { Component } from 'jails-js'
import { cancelable } from 'jails.stdlib/cancelable'
import { myService } from '../../services/my-service'

export default function myComponent({
	main,
	on,
	state,
	unmount,
}: Component) {
	let unsubscribe: (() => void) | undefined

	// Create a cancelable async operation
	const performAsyncTask = cancelable(async (input: string) => {
		try {
			const result = await myService.fetchData({ input })
			// Safe to update state; only called if not cancelled
			await updateState(result)
		} catch (error) {
			// Abort errors are silently ignored by cancelable
			if (error instanceof Error) {
				console.error('Task failed:', error.message)
			}
		}
	})

	main(() => {
		on('submit', 'form', handleSubmit)
		unsubscribe = store.subscribe(updateComponent)
	})

	unmount(() => {
		// Cancelable automatically cleans up pending operations
		unsubscribe?.()
	})

	const handleSubmit = async (event: Event) => {
		event.preventDefault()
		const form = event.target as HTMLFormElement
		const input = new FormData(form).get('search') as string

		// Call the cancelable function
		// If a previous call is still pending, it will be cancelled
		await performAsyncTask(input)
	}
}
```

### Key benefits

1. **Automatic cancellation**: Calling the function again cancels the previous request
2. **Safe error handling**: Cancelled requests don't trigger error handlers or state updates
3. **Unmount safety**: Pending requests are automatically aborted when the component unmounts
4. **API signal propagation**: The underlying `AbortSignal` is passed to `fetch()` via the `signal` option

### Service integration

Services must accept and use the `signal` parameter from `cancelable`:

```typescript
// In src/domain/weather/services/open-meteo/index.ts
export const searchLocation = async ({
	query,
	signal,
}: SearchLocationInput): Promise<SearchLocationResult> => {
	const url = new URL(geocodingEndpoint)
	url.searchParams.set('name', query)

	// Pass signal to fetch to enable cancellation
	const response = await fetch(url, signal ? { signal } : undefined)
	// ... rest of implementation
}
```

This allows the network request to be cancelled when:
- A new search is triggered before the previous one completes
- The component unmounts
- The user navigates away

### Without cancelable (anti-pattern)

Do not manually manage abort signals with `AbortController` in component controllers:

```typescript
// ❌ Anti-pattern: Manual abort management
let activeRequest: AbortController | undefined
let mounted = true

unmount(() => {
	mounted = false
	activeRequest?.abort()
})

const submit = async () => {
	activeRequest?.abort()
	const request = new AbortController()
	activeRequest = request

	try {
		const result = await myService.fetchData({
			signal: request.signal
		})
		if (!mounted || request.signal.aborted) return
		updateState(result)
	} catch (error) {
		if (!mounted || request.signal.aborted) return
		handleError(error)
	}
}
```

This pattern is error-prone:
- Requires manual state management (`mounted`, `activeRequest`)
- Race conditions between abort and state checks
- Boilerplate for each async operation
- Harder to test and reason about

### When to use cancelable

Use `cancelable` for:
- Form submissions that trigger API calls
- Search/autocomplete inputs
- Any user action that cancels a previous pending action
- Long-running background tasks that should stop on unmount

Do not use for:
- Operations that must complete regardless (like final saves)
- Operations without a natural cancellation point
- Simple one-time initialization calls

For other patterns, use standard `try/catch` with appropriate unmount guards.
