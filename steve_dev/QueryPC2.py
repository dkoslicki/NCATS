import requests
import sys

class QueryPC2:
    API_BASE_URL = 'http://www.pathwaycommons.org/pc2'

    @staticmethod
    def send_query_get(handler, url_suffix):
        url_str = QueryPC2.API_BASE_URL + "/" + handler + "?" + url_suffix
        print(url_str)
        res = requests.get(url_str)
        assert 200 == res.status_code
        return res

    @staticmethod
    def pathway_to_uniprot_ids(pathway_reactome_id):
        query_str = "uri=http://identifiers.org/reactome/" + pathway_reactome_id + "&format=TXT"
        res = QueryPC2.send_query_get("get", query_str)
        start_capturing = False
        res_text = res.text
        res_set = set()
        for line_str in res_text.splitlines():
            if start_capturing:
                fields = line_str.split("\t")[3].split(":")
                if len(fields) < 2:
                    print(line_str)
                    exit()
                else:
                    if fields[0] == "uniprot knowledgebase":
                        res_set.add(fields[1])
            if line_str.split("\t")[0] == "PARTICIPANT":
                start_capturing = True
        return res_set

    @staticmethod
    def uniprot_id_to_reactome_pathways(uniprot_id):
        res = QueryPC2.send_query_get("search.json", "q=" + uniprot_id + "&type=pathway")
        res_dict = res.json()
        search_hits = res_dict["searchHit"]
        pathway_list = [item.split("http://identifiers.org/reactome/")[1] for i in range(0, len(search_hits)) for item
                        in search_hits[i]["pathway"]]
        return set(pathway_list)

    @staticmethod
    def test():
        print(QueryPC2.uniprot_id_to_reactome_pathways("P68871"))
        print(QueryPC2.pathway_to_uniprot_ids("R-HSA-168249"))

if "--test" in set(sys.argv):
    QueryPC2.test()
