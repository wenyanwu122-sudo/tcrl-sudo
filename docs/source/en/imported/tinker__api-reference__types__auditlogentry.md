# tinker.types.AuditLogEntry

## *class* [**tinker.types.AuditLogEntry**](https://github.com/thinking-machines-lab/tinker/blob/main/src/tinker/types/audit_log_entry.py\#L10)(*BaseModel*)[​](\#class-tinkertypesauditlogentrybasemodel)

A single entry in the audit log.

**Fields:**

- **timestamp**
  
  – When the event occurred.
- **event**
  
  – The event type identifier.
- **model_id**
  
  – The model ID associated with the event, if any.
- **tinker_path**
  
  – The tinker path associated with the event, if any.
- **purpose**
  
  – The purpose of the event, if any.
