from flask import request

def get_client_ip(req=None):
    """
    Safely extract the real client IP address from the request in a production environment 
    (behind Vercel/Render proxies) or local development.
    
    Priority:
    1. HTTP_X_FORWARDED_FOR (List of IPs, take the first one)
    2. HTTP_X_REAL_IP
    3. request.remote_addr (Fallback)
    """
    if req is None:
        req = request
        
    forwarded_for = req.headers.get('X-Forwarded-For')
    if forwarded_for:
        # X-Forwarded-For can be a comma-separated list of IPs. The first is the original client.
        return forwarded_for.split(',')[0].strip()
        
    real_ip = req.headers.get('X-Real-IP')
    if real_ip:
        return real_ip.strip()
        
    return req.remote_addr
