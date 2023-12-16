import arxiv
from dataclasses import dataclass


class ARXIV:
    def __init__(self, config):
        self.config = config.arxiv_search
        self.sort_criterions = {
            'relevance' : arxiv.SortCriterion.Relevance,
            'submitted_date' : arxiv.SortCriterion.SubmittedDate,
            'last_updated' : arxiv.SortCriterion.LastUpdatedDate, 
        }
        self.sort_orders = {
            'ascending' : arxiv.SortOrder.Ascending,
            'descending' : arxiv.SortOrder.Descending,
        }
        
        self.client = arxiv.Client()
        
    def search(self, query):
        # See if the passed query is an arxiv id rather than a title.
        id_list = []
        results = []
        
        if len(query.split('.')) > 1:
            id_list.append(query)
        
        if len(id_list) > 0:
            search = arxiv.Search(
                id_list=id_list, 
                max_results=self.config.max_results, 
                sort_by=self.sort_criterions[self.config.sort_by], 
                sort_order=self.sort_orders[self.config.sort_order]
            )
        else:
            search = arxiv.Search(
                query=query, 
                max_results=self.config.max_results, 
                sort_by=self.sort_criterions[self.config.sort_by], 
                sort_order=self.sort_orders[self.config.sort_order]
            )
        
        for result in self.client.results(search):
            results.append(result)

        return results
    
    def download(self, arxiv_result):
        write_path = arxiv_result.download_pdf(dirpath=self.config.paper_dump_path)
        return write_path