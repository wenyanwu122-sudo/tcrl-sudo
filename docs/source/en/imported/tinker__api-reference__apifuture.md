# APIFuture

## *class* [**tinker.APIFuture**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/lib/public_interfaces/api_future.py)(...)[​](\#class-tinkerapifuture)

Abstract base class for futures that can be awaited or accessed synchronously.

APIFuture provides a unified interface for handling async operations that can be accessed both synchronously (via result()) and asynchronously (via await or result_async()). This allows for flexible usage patterns in both sync and async contexts.

The future can be awaited directly in async contexts:

```
result = await api_future  # Equivalent to await api_future.result_async()
```

**Or accessed synchronously:**

```
result = api_future.result()  # Blocks until complete
```

```
# In async contextfuture = training_client.forward_backward(data, "cross_entropy")result = await future  # Or await future.result_async()# In sync contextfuture = training_client.forward_backward(data, "cross_entropy")result = future.result()
```
