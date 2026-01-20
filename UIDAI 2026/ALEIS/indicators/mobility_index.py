def mobility_index(address_updates, mobile_updates, weights):
    return (
        address_updates * weights["address_weight"]
        + mobile_updates * weights["mobile_weight"]
    )
