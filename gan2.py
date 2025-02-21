from diagrams import Diagram, Edge, Node

diag = Diagram(filename="gan_simple", show=False)

# Define nodes
generator = Node("Noise Input")
latent_space = Node("Latent Space")
generated_data = Node("Generated Data")
real_data = Node("Real Data")
discriminate_real = Node("Discriminate Real")
discriminate_fake = Node("Discriminate Fake")

# Connect nodes
diag << generator >> latent_space >> generated_data
diag << real_data >> discriminate_real
diag << generated_data >> discriminate_fake

# Connect Generator and Discriminator with arrows
diag << generator - Edge(label="Noise") >> latent_space
diag << latent_space - Edge(label="Generate") >> generated_data
diag << real_data - Edge(style="dashed", label="Real Data") >> discriminate_real
diag << generated_data - Edge(style="dashed", label="Generated Data") >> discriminate_fake

# Add title and labels
diag.title("Generative Adversarial Network (GAN)")
diag.label("Loss") << discriminate_real
diag.label("Loss") >> discriminate_fake

# Render the diagram
diag.render()

