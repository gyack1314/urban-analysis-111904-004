import json,unittest,tempfile,shutil
from pathlib import Path
import pyarrow.parquet as pq
from materials.physical import load_inventory
ROOT=Path(__file__).resolve().parents[1]
class InputMaterials(unittest.TestCase):
    def test_json_parquet_values_and_inventory(self):
        self.assertTrue(load_inventory(ROOT/'inputs'))
        seed=json.loads((ROOT/'inputs/seed.json').read_text(encoding='utf-8'))
        for name,rows in seed.items():self.assertEqual(pq.read_table(ROOT/'inputs'/(name+'.parquet')).to_pylist(),rows,name)
    def test_modified_raw_file_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'inputs';shutil.copytree(ROOT/'inputs',target)
            inv=json.loads((target/'inventory.json').read_text(encoding='utf-8'))
            p=target/inv['files'][0]['path'];p.write_bytes(p.read_bytes()+b'x')
            with self.assertRaisesRegex(ValueError,'摘要'):load_inventory(target)
    def test_domain_material_references_and_edge_states(self):
        seed=json.loads((ROOT/'inputs/seed.json').read_text(encoding='utf-8'))
        actions=json.loads((ROOT/'inputs/actions.json').read_text(encoding='utf-8'))
        tasks={x['task'] for x in seed['tasks']};resources={x['resource'] for x in seed['resources']}
        self.assertTrue(all(x['predecessor'] in tasks and x['successor'] in tasks for x in seed['links']))
        self.assertTrue(all(x['resource'] in resources for x in seed['tasks']))
        self.assertTrue(all(0<=x['accepted_quantity']<=x['physical_quantity']<=100 for x in seed['progress']))
        self.assertTrue(any(x['ended'] is None and x['censored_at'] is not None for x in seed['history']))
