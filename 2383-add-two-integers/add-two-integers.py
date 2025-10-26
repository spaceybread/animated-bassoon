class Solution:
    def sum(self, a: int, b: int) -> int:
        import subprocess, json
        return int(subprocess.check_output(
            ["python3", "-c", f"print({a}+{b})"]
        ))