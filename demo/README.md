# Two ways to generate citation map
Go to [README](../README.md), set up the environment.

## Fetch through Google Scholar ID
In `demo/demo.py`, fill in the correct scholar_id. The `python demo.py`
```py
scholar_id = 'xx' # the scholars' user id in Google scholar. For example, the user id is 1AuLIv0AAAAJ in "https://scholar.google.com/citations?user=1AuLIv0AAAAJ&hl=en"
generate_citation_map(scholar_id, output_path='citation_map.html',
                    cache_folder='cache', affiliation_conservative=False, num_processes=16,
                    use_proxy=False, pin_colorful=True, print_citing_affiliations=True, 
                    use_open_alex=False)
```

## Fetch through Open Alex
Go to `https://openalex.org/`, search papers using title and get their work_id. Click 'API' as follows and you will know a paper's work_id

![alt text](../assets/image.png)
```
scholar_id = 'xx'
# 'use_open_alex' should be True, 'alex_works_id' should be an array containing id and title of scholar's works.
generate_citation_map(scholar_id, output_path='citation_map.html',
                    cache_folder='cache', affiliation_conservative=False, num_processes=16,
                    use_proxy=False, pin_colorful=True, print_citing_affiliations=True, 
                    use_open_alex=True,
                    alex_works_id = [("W4390141653", "Application of computer simulation to model transient vibration responses of GPLs reinforced doubly curved concrete panel under instantaneous heating"),
                                    ("W4390626484", "Evaluation and Improvement of Carrying Capacity of a Traffic System"),
                                    ("W4390620274", "Design of Traffic Improvement Plan for Line 1 Baijiahu Station of Nanjing Metro"),
                                    ("W4401486694", "Developments and evolution of housing architecture in the post-Corona era with a health-oriented approach")
                                    ])
```



