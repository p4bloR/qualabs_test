class SetCover():

  @classmethod
  def remove_duplicates(cls, lst):
    uniques = list(dict.fromkeys(lst))
    return uniques

  @classmethod
  def get_subsets_scores(cls, subsets, to_cover):
    scores = []
    for subset in subsets:
      scores.append(len(set(subset) & set(to_cover)))
    return scores
  
  @classmethod
  def get_most_valuable_index(cls, subsets, to_cover):
    values = SetCover.get_subsets_scores(subsets, to_cover)
    return values.index(max(values))

  @classmethod
  def remove_covered(cls, to_cover, subset):
    to_cover = [x for x in to_cover if x not in subset]
    return to_cover
    
  @classmethod
  def set_cover(cls, universe = [], subsets = [[]]):
    to_cover = SetCover.remove_duplicates(universe)
    flat_subsets = [item for subset in subsets for item in subset]
    flat_subsets = SetCover.remove_duplicates(flat_subsets)
      
    #make sure subsets cover the universe
    if set(universe).issubset(set(flat_subsets)):      
      cover_indexes = []
      
      while (len(to_cover) > 0):
        index = SetCover.get_most_valuable_index(subsets, to_cover)
        to_cover = SetCover.remove_covered(to_cover, subsets[index])
        cover_indexes.append(index)
      return cover_indexes
    else:
      return False