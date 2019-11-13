def organise_mess(input_data, nesting_levels) -> dict:
    def create_dict(tmp_dict, tmp_list):
        if len(tmp_list) > 1:
            return {tmp_dict.pop(tmp_list[0]): create_dict(tmp_dict, tmp_list[1:])}
        else:
            return {tmp_dict.pop(tmp_list[0]): [tmp_dict]}
    final_dict = dict()
    for item in input_data:
        new_dict = create_dict(item, nesting_levels)
        key = list(new_dict.keys())[0]
        if key not in final_dict.keys():
            final_dict.update(new_dict)
        else:
            t_dict = final_dict.get(key)
            n_dict = new_dict.get(key)
            for i in range(1, len(nesting_levels)):
                key = list(n_dict.keys())[0]
                if key not in t_dict.keys():
                    t_dict.update(n_dict)
                else:
                    t_dict = t_dict.get(key)
                    n_dict = n_dict.get(key)
            if isinstance(t_dict, list):
                if isinstance(n_dict, dict):
                    t_dict.append(n_dict.get(key)[0])
                else:
                    t_dict.append(n_dict[0])
    return final_dict


input_dict = [
 {
    "weapon": "Sniper Rifle",
    "city": "Manchester",
    "victim": "Moriarty",
    "age": 40
 },

 {
    "weapon": "Knife",
    "city": "Paris",
    "victim": "Maggy",
    "age": 20
 },

 {
    "weapon": "Knife",
    "city": "Lyon",
    "victim": "Maggy",
    "age": 30
 },

 {
    "weapon": "Hand Gun",
    "city": "Madrid",
    "victim": "Maggy",
    "age": 31
 },

 {
    "weapon": "Axe",
    "city": "London",
    "victim": "Watson",
    "age": 32
 },

 {
    "weapon": "Axe",
    "city": "London",
    "victim": "Irene Adler",
    "age": 33
 }
]

output_one = {
    "Moriarty": {
        "Sniper Rifle": {
            "Manchester": [
                {"age": 40}
            ]
        }
    },
    "Maggy": {
        "Knife": {
            "Paris": [
                {"age": 20}
            ],
            "Lyon": [
                {"age": 30}
            ]
        },
        "Hand Gun": {
            "Madrid": [
                {"age": 31}
            ]
        }
    },
    "Watson": {
        "Axe": {
            "London": [
                {"age": 32}
            ]
        }
    },
    "Irene Adler": {
        "Axe": {
            "London": [
                {"age": 33}
            ]
        }
    }
}

output_two = {
    "Moriarty": {
        "Sniper Rifle": [
            {
                "city": "Manchester",
                "age": 40
            }
        ]
    },
    "Maggy": {
        "Knife": [
            {
                "city": "Paris",
                "age": 20
            },
            {
                "city": "Lyon",
                "age": 30
            }
        ],
        "Hand Gun": [
            {
                "city": "Madrid",
                "age": 31
            }
        ]
    },
    "Watson": {
        "Axe": [
            {
                "city": "London",
                "age": 32
            }
        ]
    },
    "Irene Adler": {
        "Axe": [
            {
                "city": "London",
                "age": 33
            }
        ]
    }
}

import copy

assert organise_mess(copy.deepcopy(input_dict), ['victim', 'weapon', 'city']) == output_one
assert organise_mess(copy.deepcopy(input_dict), ['victim', 'weapon']) == output_two
print("Success!!")

