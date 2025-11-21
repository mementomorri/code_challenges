def filtered_accumulate(combiner, null_value, term, a, next, b, filter):
    if a > b:
        return null_value

    if filter(a):
        return combiner(
            term(a),
            filtered_accumulate(combiner, null_value, term, next(a), next, b, filter),
        )

    return filtered_accumulate(combiner, null_value, term, next(a), next, b, filter)
