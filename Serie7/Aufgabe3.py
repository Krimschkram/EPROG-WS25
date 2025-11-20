def merge(l1, l2):
    i = j = 0
    merged = []

    # Solange beide Listen noch Elemente haben
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    # Falls eines der beiden Reste hat
    merged.extend(l1[i:])
    merged.extend(l2[j:])

    return merged


def merge_sort(liste):
    # Fall 1: Liste ist bereits sortiert (0 oder 1 Element)
    if len(liste) <= 1:
        return liste

    # Liste halbieren
    mitte = len(liste) // 2
    links = liste[:mitte]
    rechts = liste[mitte:]

    # Rekursion
    links_sortiert = merge_sort(links)
    rechts_sortiert = merge_sort(rechts)

    # Merge der zwei sortierten Listen
    return merge(links_sortiert, rechts_sortiert)


