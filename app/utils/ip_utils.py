from flask import request, has_request_context

def extract_real_ip():
    """
    Extracts the real client IP address from the Flask request object.
    
    Logic Priority:
    1. Check 'X-Forwarded-For' (common behind AWS ELB, Nginx). 
       It returns a comma-separated list of IPs. The first one is the original client.
    2. Check 'X-Real-IP' (common in Nginx proxying).
    3. Fallback to `request.remote_addr` for local development or direct access.
    
    Security Consideration:
    If running behind a proxy in production, ensure that the proxy strips out 
    user-supplied X-Forwarded-For headers to prevent spoofing, or use a tool 
    like Werkzeug's ProxyFix to securely parse trusted forward headers only.
    """
    # 0. Check for request context (safety for background tasks)
    if not has_request_context():
        return '127.0.0.1' # Default for CLI/background jobs

    # 1. Check if X-Forwarded-For exists
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        # X-Forwarded-For can be a comma-separated list: "client, proxy1, proxy2"
        # We want the first IP which is the original client
        return x_forwarded_for.split(',')[0].strip()
    
    # 2. Check X-Real-IP
    x_real_ip = request.headers.get('X-Real-IP')
    if x_real_ip:
        return x_real_ip.strip()
    
    # 3. Fallback to direct connection IP (local development)
    return request.remote_addr or 'Unknown'
