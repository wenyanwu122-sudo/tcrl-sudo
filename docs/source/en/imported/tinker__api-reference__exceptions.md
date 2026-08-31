# tinker._exceptions

Exception hierarchy for the Tinker SDK. All exceptions inherit from `TinkerError`.

```
TinkerError├── APIError│   ├── APIResponseValidationError│   ├── APIStatusError│   │   ├── BadRequestError (400)│   │   ├── AuthenticationError (401)│   │   ├── PermissionDeniedError (403)│   │   ├── NotFoundError (404)│   │   ├── ConflictError (409)│   │   ├── UnprocessableEntityError (422)│   │   ├── RateLimitError (429)│   │   └── InternalServerError (500+)│   └── APIConnectionError│       └── APITimeoutError├── SidecarError│   ├── SidecarStartupError│   ├── SidecarDiedError│   └── SidecarIPCError└── RequestFailedError
```

| Exception | Base | Description |
| --- | --- | --- |
| TinkerError | Exception | Base exception for all Tinker-related errors. |
| APIError | TinkerError | Base class for all API-related errors. |
| APIResponseValidationError | APIError | Raised when API response doesn't match expected schema. |
| APIStatusError | APIError | Raised when an API response has a status code of 4xx or 5xx. |
| APIConnectionError | APIError | Raised when a connection error occurs while making an API request. |
| APITimeoutError | APIConnectionError | Raised when an API request times out. |
| BadRequestError | APIStatusError | HTTP 400: The request was invalid or malformed. |
| AuthenticationError | APIStatusError | HTTP 401: Authentication credentials are missing or invalid. |
| PermissionDeniedError | APIStatusError | HTTP 403: Insufficient permissions to access the resource. |
| NotFoundError | APIStatusError | HTTP 404: The requested resource was not found. |
| ConflictError | APIStatusError | HTTP 409: The request conflicts with the current state of the resource. |
| UnprocessableEntityError | APIStatusError | HTTP 422: The request was well-formed but contains semantic errors. |
| RateLimitError | APIStatusError | HTTP 429: Too many requests, rate limit exceeded. |
| InternalServerError | APIStatusError | HTTP 500+: An error occurred on the server. |
| SidecarError | TinkerError | Base exception for subprocess sidecar errors. |
| SidecarStartupError | SidecarError | Raised when the sidecar subprocess fails to start or times out. |
| SidecarDiedError | SidecarError | Raised when the sidecar subprocess exits unexpectedly while requests are pending. |
| SidecarIPCError | SidecarError | Raised when communication with the sidecar subprocess fails. |
| RequestFailedError | TinkerError | Raised when an asynchronous request completes in a failed state. |
