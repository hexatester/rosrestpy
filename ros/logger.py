# Logging Client Library
#
# (c) 2023 Icosa Consulting Inc.
#
"""
        Logging Base Class
        Initializes:
               SysLog, ConsoleLog, FileLog

"""
# System Imports
import os
import socket
import getpass
import logging
import logging.config
from logging.handlers import SysLogHandler, RotatingFileHandler
from attr import define
from typing import Any, List

class SysLogger:
	"""
	Global System Logger Module
	"""
	name: str
	loglevel: int
	format: str = None
	_handlers: List = None
	_logger: logging = None
	_format: str = None

	class FileLogFilter(logging.Filter):
		"""
		Add extra info to file logging
		"""
		app: Any = None

		def __init__(self, app: Any = None):
			self.app = app

		def filter(self, record):
			return True

	class ConsoleLogFilter(logging.Filter):
		"""
		Add extra info to console logging
		"""
		app: Any = None

		def __init__(self, app: Any = None):
			self.app = app

		def filter(self, record):
			return True

	def __init__(self, name: str, loglevel: int, format: str = None):
		"""
		Initialize logging handler
		"""
		self._handlers = []
		self._logger = None
		self._format = None

		logger = logging.getLogger(name)
		logger.setLevel(loglevel)

		self._logger = logger
		self._name = (name or logger.name)

		if format is None:
			format = self.console_format

		logfmt = logging.Formatter(format)
		self._format = logfmt

		# Only add the handler once per instance
		if (logger.hasHandlers()):
			hnames = [h.name for h in self._handlers]
			for h in logger.handlers:
				if (h.name in hnames):
					logger.removeHandler(h)
					logger.debug('Removed %s', h.name)

		self.add_stdout()

	@property
	def default_format(self) -> str:
		return '%(asctime)s | %(process)d | %(module)-14s | %(levelname)s - %(message)s'

	@property
	def console_format(self) -> str:
		return '%(asctime)s | %(name)s.%(module)-12s | %(levelname)s - %(message)s'

	@property
	def syslog_format(self) -> str:
		return '| %(process)d | %(name)s.%(funcName)-12s | %(levelname)s - %(message)s'

	@property
	def thread_format(self) -> str:
		return '%(asctime)s | %(threadName)-11s | %(module)-14s | %(levelname)s - %(message)s'

	@property
	def syslogger(self) -> logging:
		return self._logger

	@property
	def syshandlers(self) -> logging.handlers:
		return self._handlers

	@syshandlers.setter
	def syshandlers(self, key, value):
		self._handlers[key] = value

	@property
	def loggername(self):
		return self._name

	@staticmethod
	def new_logger(name=__name__):
		return logging.getLogger(name)

	def log_message(self, message, level=None):
		if not level:
			level = self._logger.level
		if level == logging.INFO:
			return self._logger.info(message)
		elif level == logging.WARN:
			return self._logger.warning(message)
		elif level == logging.ERROR:
			return self._logger.error(message)
		elif level == logging.CRITICAL:
			return self._logger.critical(message)
		elif level == logging.DEBUG:
			return self._logger.debug(message)

	def new_session(self, name=__name__):
		self.syslogger.info('-----> Logging session started [%s] User [%s] <-----', name, getpass.getuser())

	def _add_handler(self, handler):
		"""
		Add and save the handler
		"""
		if handler.name not in self.syshandlers:
			self.syshandlers.append(handler.name)
			self._logger.addHandler(handler)

			self.syslogger.debug('Logging Handler %s added', handler.name)

	def _update_handler(self, handler, format=None, level=None):
		"""
		Set handler format and log level
		"""
		if not handler:
			self.syslogger.warning('Handler not updated')
			return

		if (self._format and (not format)):
			format = self._format

		if format:
			if isinstance(format, str):
				format = logging.Formatter(format)
			handler.setFormatter(format)

		if level:
			handler.setLevel(level)

	def add_filelog(self, filename, format=None, level=None, maxsize=16384, count=5, perms=0o770):
		"""
		Add a Rotating File Handler
		"""
		name = self.loggername
		path = None
		handler = None

		if format is None:
			format = self.default_format

		try:
			path = os.path.dirname(os.path.realpath(filename))
			if not os.path.exists(path):
				os.mkdir(path, perms)

			handler = RotatingFileHandler(filename=filename, maxBytes=maxsize, backupCount=count)
			handler.set_name(f'FILELOG_{name}')
			handler.addFilter(self.FileLogFilter())

			self._update_handler(handler, format)
			self._add_handler(handler)

		except OSError as e:
			self.syslogger.warning(e)
			self.syslogger.error('No log directory created')

	def add_syslog(self, address=None, level=None, format=None, port=514):
		"""
		Add a Syslog Handler
		"""
		name = self.loggername
		syslogger = '/dev/log'

		if address is None:
			if (os.path.exists(syslogger)):
				address=syslogger

		if format is None:
			format = self.syslog_format

		handler = SysLogHandler(address=(address, port))
		handler.set_name(f'SYSLOG_{name}')

		self._update_handler(handler, socket.gethostname() + format)
		self._add_handler(handler)

	def add_stdout(self, out=None, format=None):
		"""
		Add STD.out handler
		"""
		name = self.loggername

		if format is None:
			format = self.console_format

		handler = logging.StreamHandler(stream=out)
		handler.set_name(f'STDLOG_{name}')
		handler.addFilter(self.ConsoleLogFilter())

		self._update_handler(handler, format)
		self._add_handler(handler)
