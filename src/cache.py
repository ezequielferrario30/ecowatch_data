from collections import deque, defaultdict
from datetime import datetime, timedelta

class RecentLogsCache:
    def __init__(self, window_minutes=5):
        self.window = timedelta(minutes=window_minutes)
        self.logs = deque()
        self.logs_by_sala = defaultdict(list)
        self.logs_by_timestamp = defaultdict(list)
        self.latest_timestamp = None

    def add_log(self, log):
        log_time = datetime.fromisoformat(log["timestamp"])
        self.logs.append((log_time, log))
        self.logs_by_sala[log["sala"]].append(log)
        self.logs_by_timestamp[log["timestamp"]].append(log)
        # Actualiza el timestamp más reciente al agregar un log
        if self.latest_timestamp is None or log_time > self.latest_timestamp:
            self.latest_timestamp = log_time
        self._cleanup()

    def _cleanup(self):
        """Limpia usando el timestamp más reciente como referencia, no el reloj del sistema."""
        if not self.latest_timestamp:
            return
        while self.logs and (self.latest_timestamp - self.logs[0][0]) > self.window:
            old_time, old_log = self.logs.popleft()
            self.logs_by_sala[old_log["sala"]].remove(old_log)
            self.logs_by_timestamp[old_log["timestamp"]].remove(old_log)

    def query_by_sala(self, sala):
        return list(self.logs_by_sala.get(sala, []))

    def query_by_timestamp(self, timestamp):
        return list(self.logs_by_timestamp.get(timestamp, []))
