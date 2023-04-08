import os
from article_combiner import ArticleCombiner
from article_pruner import ArticlePruner

filename = "all_articles"
keywords = ["cat", "dog"]

ArticleCombiner(os.getcwd(), filename)
ArticlePruner(keywords, filename, f"{filename}-pruned")




