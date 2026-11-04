"""
Serviço responsável pelos cálculos de negócio
"""


def get_completed(df):
    return df[df["status"] == "completed"]


def total_revenue(df):

    df = get_completed(df)

    return round(
        df["revenue"].sum(),
        2
    )


def total_orders(df):

    df = get_completed(df)

    return int(df.shape[0])


def average_ticket(df):

    df = get_completed(df)

    if len(df) == 0:
        return 0

    return round(
        df["revenue"].sum() / len(df),
        2
    )


def unique_customers(df):

    df = get_completed(df)

    return df["customer_id"].nunique()


def cancellation_rate(df):

    total = df.shape[0]

    canceled = df[
        df["status"] == "canceled"
    ].shape[0]

    if total == 0:
        return 0

    return round(
        (canceled / total) * 100,
        2
    )


def revenue_per_customer(df):

    revenue = total_revenue(df)

    customers = unique_customers(df)

    if customers == 0:
        return 0

    return round(
        revenue / customers,
        2
    )
    def get_revenue_by_period(
    df,
    start_date,
    end_date
):
    """
    Retorna a receita dentro de um período.
    """

    df = get_completed(df)

    filtered = df[
        (df["date"] >= start_date)
        &
        (df["date"] <= end_date)
    ]

    return round(
        filtered["revenue"].sum(),
        2
    )
