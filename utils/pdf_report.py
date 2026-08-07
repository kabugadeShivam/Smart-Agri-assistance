from reportlab.platypus import *

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.units import inch

styles = getSampleStyleSheet()


def create_report(

    filename,

    fertilizer,

    disease,

    confidence,

    weather,

    yield_prediction,

    production,

    revenue,

    recommendations,

    score

):

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph("<b>SMART AGRICULTURE AI REPORT</b>", styles["Title"])
    )

    story.append(Spacer(1,0.25*inch))

    story.append(
        Paragraph(f"<b>Recommended Fertilizer:</b> {fertilizer}",styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Disease:</b> {disease}",styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Confidence:</b> {confidence:.2f}%",styles["BodyText"])
    )

    if weather:

        story.append(
            Paragraph(

                f"<b>Weather:</b> {weather['weather']} | {weather['temperature']}°C | {weather['humidity']}%",

                styles["BodyText"]

            )
        )

    story.append(
        Paragraph(f"<b>Yield:</b> {yield_prediction:.2f} ton/hectare",styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Production:</b> {production:.2f} ton",styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Revenue:</b> ₹ {revenue:,.0f}",styles["BodyText"])
    )

    story.append(Spacer(1,0.2*inch))

    story.append(
        Paragraph("<b>AI Recommendations</b>",styles["Heading2"])
    )

    for r in recommendations:

        story.append(
            Paragraph("• "+r,styles["BodyText"])
        )

    story.append(Spacer(1,0.2*inch))

    story.append(
        Paragraph(f"<b>Farm Health Score:</b> {score}/100",styles["Heading2"])
    )

    doc.build(story)