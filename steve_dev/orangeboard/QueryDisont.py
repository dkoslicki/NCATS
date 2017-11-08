import requests
import functools
import CachedMethods


class QueryDisont:

    API_BASE_URL = 'http://www.disease-ontology.org/api'

    @staticmethod
    def send_query_get(handler, url_suffix): 
        url_str = QueryDisont.API_BASE_URL + "/" + handler + "/" + url_suffix
#        print(url_str)
        res = requests.get(url_str, headers={'accept': 'application/json'})
        assert res.status_code == 200
        return res
    
    @staticmethod
    @CachedMethods.register
    @functools.lru_cache(maxsize=1024, typed=False)
    def query_disont_to_child_disonts(disont_id):
        res_json = QueryDisont.send_query_get('metadata', 'DOID:' + str(disont_id)).json()
#        print(res_json)
        disease_children_list = res_json.get("children", None)
        if disease_children_list is not None:
            return set([int(disease_child_list[1].split(':')[1]) for disease_child_list in disease_children_list])
        else:
            return set()

    @staticmethod
    @CachedMethods.register
    @functools.lru_cache(maxsize=1024, typed=False)
    def query_disont_to_child_disonts_desc(disont_id):
        res_json = QueryDisont.send_query_get('metadata', 'DOID:' + str(disont_id)).json()
#        print(res_json)
        disease_children_list = res_json.get("children", None)
        if disease_children_list is not None:
            return dict([[int(disease_child_list[1].split(':')[1]), disease_child_list[0]] for disease_child_list in disease_children_list])
        else:
            return dict()
         
    @staticmethod
    @CachedMethods.register
    @functools.lru_cache(maxsize=1024, typed=False)
    def query_disont_to_mesh_id(disont_id):
        res_json = QueryDisont.send_query_get('metadata', 'DOID:' + str(disont_id)).json()
        xref_strs = res_json["xrefs"]
        mesh_ids = set([xref_str.split('MESH:')[1] for xref_str in xref_strs if 'MESH:' in xref_str])
        return mesh_ids
        
    @staticmethod
    def test():
        print(QueryDisont.query_disont_to_mesh_id(14069))
        print(QueryDisont.query_disont_to_child_disonts_desc(12365))
        
if __name__ == '__main__':
    QueryDisont.test()
    
