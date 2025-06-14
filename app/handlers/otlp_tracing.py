import logging
from opentelemetry import metrics, trace

from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter,
)
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource

def configure_oltp_grpc_tracing(
    endpoint: str = None
) -> trace.Tracer:
    # Configure Tracing
    traceProvider = TracerProvider(resource=Resource({"service.name": "fastapi_aspire_dashboard"}))
    processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=endpoint))
    traceProvider.add_span_processor(processor)
    trace.set_tracer_provider(traceProvider)

    # Configure Metrics
    reader = PeriodicExportingMetricReader(OTLPMetricExporter(endpoint=endpoint))
    meterProvider = MeterProvider(metric_readers=[reader], resource=Resource({"service.name": "fastapi_aspire_dashboard"}))
    metrics.set_meter_provider(meterProvider)

    # Configure Logging
    logger_provider = LoggerProvider(resource=Resource({"service.name": "fastapi_aspire_dashboard"}))
    set_logger_provider(logger_provider)

    exporter = OTLPLogExporter(endpoint=endpoint)
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
    handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)
    handler.setFormatter(logging.Formatter("Python: %(message)s"))

    # Attach OTLP handler to root logger
    logging.getLogger().addHandler(handler)

    tracer = trace.get_tracer(__name__)
    return tracer