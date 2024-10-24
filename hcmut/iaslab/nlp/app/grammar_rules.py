# grammar_rules.py

grammar_rules = """
S -> NP VP
NP -> Det N
VP -> V NP | V Adj
Det -> 'một' | 'những' | 'các' | 'mỗi' | 'tất_cả' | 'mọi' | 'một_số' | 'một_vài' | 'một_ít' | 'một_chút' | 'một_lúc' | 'một_cách' | 'một_chút'
N -> 'khách_hàng' | 'sản_phẩm' | 'nhu_cầu' | 'dịch_vụ'
V -> 'có' | 'muốn' | 'cần' | 'quan_tâm' | 'bận' | 'không_bận' | 'thích' | 'không_thích' | 'hài_lòng' | 'không_hài_lòng' | 'đánh_giá' | 'không_đánh_giá' | 'thích_thú'
Adj ->  'tốt' | 'kém' | 'khác' | 'đa_dạng' | 'độc_đáo' | 'chất_lượng' | 'tệ' | 'tinh_tế' | 'đẹp' | 'xấu' | 'rẻ' | 'đắt' | 'hợp_lý' | 'không_hợp_lý' | 'chăm_sóc' | 'nhanh' | 'chậm' | 'tận_tình'| 'tận_tâm' | 'không_tận_tâm' | 'tận_tình_chu_đáo' | 'tận_tâm_chu_đáo'| 'tận_tình_chu_đáo'| 'tận_tâm_chu_đáo' |'thoải_mái'
"""