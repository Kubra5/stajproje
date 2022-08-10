import dns.resolver
import sys

def query(domain):
    answer = dns.resolver.resolve( domain  ,'A')
    for server in answer :
        return (server.to_text())

#query("youtube.com")
