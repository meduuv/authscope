"""Offline authentication event summarization helpers."""

def summarize(events):
    result = {"total": len(events), "success": 0, "failure": 0, "principals": {}}
    for event in events:
        status = str(event.get("status", "")).lower()
        principal = str(event.get("principal", "unknown"))
        if status in ("success", "ok", "accepted"):
            result["success"] += 1
        elif status in ("failure", "failed", "denied"):
            result["failure"] += 1
        result["principals"][principal] = result["principals"].get(principal, 0) + 1
    return result

def repeated_failures(events, minimum=3):
    counts = {}
    for event in events:
        if str(event.get("status", "")).lower() in ("failure", "failed", "denied"):
            key = str(event.get("principal", "unknown"))
            counts[key] = counts.get(key, 0) + 1
    return {k: v for k, v in counts.items() if v >= minimum}
