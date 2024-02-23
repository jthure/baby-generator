import gradio as gr
from openai import OpenAI

client = OpenAI(api_key="")


def generate_image_based_on_prompt(
    kön,
    hårfärg,
    ögonfärg,
    längd,
    vikt,
    humör,
    musiksmak,
    klädstil,
    intressen,
    favoritfilm,
    favoritbok,
):
    # Assuming this function would send a request to an image-generating model, but here we'll just return a placeholder

    # Placeholder for the image URL or logic to call an actual API for image generation

    prompt = f"""Skapa en naturlig bild av en ett-årig bebis. Bebisen har {hårfärg} hår och {ögonfärg} ögon. Hen är {längd} cm lång och väger {vikt} kg. Hen är {humör} och gillar {musiksmak}. Hen klär sig i {klädstil} och gillar {intressen}. Hen gillar att titta på {favoritfilm} och läsa {favoritbok}."""
    print(prompt)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        style="vivid",
        n=1,
    )

    print(response.model_dump_json)
    image_url = response.data[0].url
    image_placeholder_url = image_url
    return image_placeholder_url


def update_image_output(
    kön,
    hårfärg,
    ögonfärg,
    längd,
    vikt,
    humör,
    musiksmak,
    klädstil,
    intressen,
    favoritfilm,
    favoritbok,
):
    # This wrapper function calls the main logic and updates the image output
    image_url = generate_image_based_on_prompt(
        kön,
        hårfärg,
        ögonfärg,
        längd,
        vikt,
        humör,
        musiksmak,
        klädstil,
        intressen,
        favoritfilm,
        favoritbok,
    )
    return gr.Image(image_url, visible=True)


def x():
    return gr.Image(None, visible=True)


# Define the interface
with gr.Blocks() as demo:
    gr.Markdown("# Bebisformuläret")
    gr.Markdown("Hur tänker du dig att din bebis ser ut när hen är ett år gammal?")

    with gr.Column():
        kön = gr.Textbox(label="Kön", placeholder="")
        hårfärg = gr.Textbox(label="Hårfärg", placeholder="")
        ögonfärg = gr.Textbox(label="Ögonfärg", placeholder="")
        längd = gr.Textbox(label="Längd", placeholder="")
        vikt = gr.Textbox(label="Vikt", placeholder="")
        humör = gr.Textbox(label="Humör", placeholder="")
        musiksmak = gr.Textbox(label="Musiksmak", placeholder="")
        klädstil = gr.Textbox(label="Klädstil/stil", placeholder="")
        intressen = gr.Textbox(label="Intressen", placeholder="")
        favoritfilm = gr.Textbox(label="Favoritfilm", placeholder="")
        favoritbok = gr.Textbox(label="Favoritbok", placeholder="")
    generate_button = gr.Button("Spara")
    image_output = gr.Image(visible=False)

    generate_button.click(
        fn=update_image_output,
        inputs=[
            kön,
            hårfärg,
            ögonfärg,
            längd,
            vikt,
            humör,
            musiksmak,
            klädstil,
            intressen,
            favoritfilm,
            favoritbok,
        ],
        outputs=image_output,
        show_progress="full",
    )

demo.launch(share=True)
