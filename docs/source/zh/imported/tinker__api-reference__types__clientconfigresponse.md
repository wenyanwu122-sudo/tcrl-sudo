# tinker.types.ClientConfigResponse

## *class* [**tinker.types.ClientConfigResponse**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/client_config_response.py\#L8)(*BaseModel*)[​](\#class-tinkertypesclientconfigresponsebasemodel)

Server-side feature flags resolved for this caller.

Uses BaseModel (extra="ignore") so new flags from the server are silently dropped until the SDK adds fields for them.

**Fields:**

- **pjwt_auth_enabled**
- **credential_default_source**
- **sample_dispatch_bytes_semaphore_size**
- **inflight_response_bytes_semaphore_size**
- **parallel_fwdbwd_chunks**
- **proto_write_fwdbwd**
  
  – When true, the SDK serializes ForwardBackwardRequest as proto bytes and POSTs with Content-Type: application/x-protobuf. Falls back to JSON when false (default) or when the request can't be encoded in proto.
- **billing_exception_max_pause_duration_sec**
- **grpc_target**
- **enable_grpc_retrieve_future**
- **sample_no_retries**
- **use_pyqwest_transport**
  
  – When true, the SDK builds its default httpx async client on top of the pyqwest (reqwest/hyper-based) transport adapter. Set to false server-side to force every client to fall back to httpx's default transport.
