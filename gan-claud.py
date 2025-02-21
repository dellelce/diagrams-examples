from diagrams import Cluster, Diagram
from diagrams.generic.device import _Device as Device
from diagrams.generic.compute import Workstation, Server
from diagrams.onprem.analytics import Tensorflow

with Diagram("Generative Adversarial Network", show=False):
    with Cluster("Generator"):
        generator = Workstation("Generator\nNeural Network")

    with Cluster("Discriminator"):
        discriminator = Workstation("Discriminator\nNeural Network")

    with Cluster("Training Data"):
        training_data = Device("Training\nData")

    with Cluster("Generated Data"):
        generated_data = Server("Generated\nData")

    training_data >> generator >> generated_data
    generated_data >> discriminator
    discriminator >> generator
