# main.py
from fastmcp import FastMCP
import psutil

# MCP 서버 인스턴스 생성
mcp = FastMCP("ResourceMonitor")

# CPU 사용량 툴 등록
@mcp.tool()
def cpu_usage() -> str:
    """CPU 사용량 (%)를 반환합니다."""
    return f"{psutil.cpu_percent(interval=1)}%"

# 메모리 사용량 툴 등록
@mcp.tool()
def memory_usage() -> str:
    """Memory 사용량 (%)를 반환합니다."""
    return f"{psutil.virtual_memory().percent}%"

# 디스크 사용량 툴 등록
@mcp.tool()
def disk_usage() -> str:
    """디스크 사용량 (%)를 반환합니다."""
    return f"{psutil.disk_usage('/').percent}%"

# 네트워크 사용량 툴 등록
@mcp.tool()
def network_usage() -> dict:
    """네트워크 송수신(MB)를 반환합니다."""
    net = psutil.net_io_counters()
    return {
        "Sent_MB": round(net.bytes_sent / (1024*1024), 2),
        "Recv_MB": round(net.bytes_recv / (1024*1024), 2)
    }

if __name__ == "__main__":
    mcp.run()  # stdio transport로 MCP 서버 실행
