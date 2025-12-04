"""
chart.py
Generate a professional Seaborn violinplot visualizing the distribution of
customer support first-response times across channels for a major retail client.
Requirements satisfied:
- Uses seaborn.violinplot()
- Realistic synthetic data for support efficiency analysis
- Professional styling (Seaborn theme, labels, title, palette)
- Figure saved as 512x512 PNG via 8x8 inches @ 64 dpi
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def generate_synthetic_support_data(seed: int = 42) -> pd.DataFrame:
    """
    Generate realistic synthetic data for customer support response times.
    Channels:
    - Email: typically slower, higher variance
    - Live Chat: fastest, tightly clustered
    - Phone: moderate response time
    - Social Media: can be slow and highly variable
    Returns a pandas DataFrame with:
    - channel: support channel category
    - response_time_min: time to first response in minutes
    """
    rng = np.random.default_rng(seed)

    n_per_channel = 400

    channels = []
    response_times = []

    # Email: mean ~45 mins, skewed right
    email_times = rng.gamma(shape=3.0, scale=15.0, size=n_per_channel)

    # Live Chat: mean ~5 mins, tight
    chat_times = rng.gamma(shape=2.0, scale=2.5, size=n_per_channel)

    # Phone: mean ~20 mins
    phone_times = rng.gamma(shape=2.5, scale=8.0, size=n_per_channel)

    # Social Media: mean ~60 mins, more variance
    social_times = rng.gamma(shape=3.0, scale=20.0, size=n_per_channel)

    channels.extend(["Email"] * n_per_channel)
    response_times.extend(email_times)

    channels.extend(["Live Chat"] * n_per_channel)
    response_times.extend(chat_times)

    channels.extend(["Phone"] * n_per_channel)
    response_times.extend(phone_times)

    channels.extend(["Social Media"] * n_per_channel)
    response_times.extend(social_times)

    df = pd.DataFrame(
        {
            "channel": channels,
            "response_time_min": response_times,
        }
    )

    # Clip extreme outliers to a business-plausible maximum (e.g., 3 hours)
    df["response_time_min"] = df["response_time_min"].clip(lower=0, upper=180)

    return df


def create_violinplot(df: pd.DataFrame, output_path: str = "chart.png") -> None:
    """
    Create and save a Seaborn violinplot visualizing response times by channel.
    - Uses Seaborn styling best practices:
      * sns.set_theme() for style + context
      * professional palette
      * informative title and axis labels
    - Export:
      * 8x8 inch figure at 64 dpi -> 512x512 pixels
      * Saved to output_path
    """

    # Professional Seaborn theme
    sns.set_theme(style="whitegrid", context="talk")

    # 8x8 inches; with dpi=64 this yields 512x512 pixels
    plt.figure(figsize=(8, 8))

    # Violinplot: distribution and quartiles per channel
    ax = sns.violinplot(
        data=df,
        x="channel",
        y="response_time_min",
        palette="muted",
        inner="quartile",
        cut=0,
    )

    # SLA threshold line (example: 30 minutes)
    sla_minutes = 30
    plt.axhline(
        sla_minutes,
        linestyle="--",
        color="red",
        alpha=0.7,
        label=f"SLA target: {sla_minutes} min",
    )

    ax.set_title(
        "Distribution of Customer Support First-Response Times by Channel",
        fontsize=16,
        weight="bold",
        pad=20,
    )
    ax.set_xlabel("Support Channel", fontsize=13)
    ax.set_ylabel("First Response Time (minutes)", fontsize=13)

    ax.set_ylim(0, 120)
    ax.legend(loc="upper right")

    plt.tight_layout()

    # Save as 512x512 PNG:
    #   8x8 inches * 64 dpi = 512x512 pixels
    plt.savefig(output_path, dpi=64, bbox_inches="tight")
    plt.close()


def main():
    df = generate_synthetic_support_data()
    create_violinplot(df, output_path="chart.png")


if __name__ == "__main__":
    main()