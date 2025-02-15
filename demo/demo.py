import sys
sys.path.insert(0, "../")
from citation_map import generate_citation_map

if __name__ == '__main__':
    # This is my Google Scholar ID. Replace this with your ID.
    scholar_id = 'xx'
    generate_citation_map(scholar_id, output_path='citation_map.html',
                          cache_folder='cache', affiliation_conservative=False, num_processes=16,
                          use_proxy=False, pin_colorful=True, print_citing_affiliations=True, 
                          use_open_alex=True,
                          alex_works_id = [("W4390141653", "Application of computer simulation to model transient vibration responses of GPLs reinforced doubly curved concrete panel under instantaneous heating"),
                                           ("W4390626484", "Evaluation and Improvement of Carrying Capacity of a Traffic System"),
                                           ("W4390620274", "Design of Traffic Improvement Plan for Line 1 Baijiahu Station of Nanjing Metro"),
                                           ("W4401486694", "Developments and evolution of housing architecture in the post-Corona era with a health-oriented approach")
                                           ])
