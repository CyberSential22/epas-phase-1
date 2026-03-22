from flask import request, has_request_context

def get_client_ip(req=None):
    """
    Extracts the real client IP address from the Flask request object.
    
    Logic Priority:
    1. Check 'X-Forwarded-For' (common behind AWS ELB, Nginx, Vercel, Render). 
       It returns a comma-separated list of IPs. The first one is the original client.
    2. Check 'X-Real-IP' (common in Nginx proxying).
    3. Fallback to `request.remote_addr` for local development or direct access.
    """
    req = req or request
    if not has_request_context():
        return '127.0.0.1'

    # 1. Check if X-Forwarded-For exists
    x_forwarded_for = req.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    
    # 2. Check X-Real-IP
    x_real_ip = req.headers.get('X-Real-IP')
    if x_real_ip:
        return x_real_ip.strip()
    
    # 3. Fallback to direct connection IP
    return req.remote_addr or '127.0.0.1'

# Maintain backward compatibility
def extract_real_ip():
    return get_client_ip(request)
