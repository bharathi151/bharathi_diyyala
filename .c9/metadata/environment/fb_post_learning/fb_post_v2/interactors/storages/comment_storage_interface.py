{"filter":false,"title":"comment_storage_interface.py","tooltip":"/fb_post_learning/fb_post_v2/interactors/storages/comment_storage_interface.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":6,"column":0},"end":{"row":8,"column":12},"action":"remove","lines":["    @abstractmethod","    def create_post(self, user_id: int, post_content: str) ->int:","        pass"],"id":2},{"start":{"row":5,"column":28},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":33,"column":0},"end":{"row":103,"column":0},"action":"remove","lines":["    @abstractmethod","    def react_to_post(self, user_id: int, post_id: int, reaction_type: str):","        pass","","    @abstractmethod","    def make_undo_to_post_reaction(self, user_id: int,","                                   post_id: int,","                                   reaction_type: str):","        pass","","    @abstractmethod","    def update_post_reaction(self, user_id: int,","                             post_id: int,","                             reaction_type: str):","        pass","","    @abstractmethod","    def is_reaction_type_existed(self, reaction_type: str) -> bool:","        pass","","    @abstractmethod","    def is_post_reaction_existed(self, user_id: int, post_id: int) -> bool:","        pass","","    @abstractmethod","    def is_reaction_type_valid(self, reaction_type: str) -> bool:","        pass","","    @abstractmethod","    def react_to_comment(self, user_id: int,","                         comment_id: int,","                         reaction_type: str):","        pass","","    @abstractmethod","    def make_undo_to_comment_reaction(self, user_id: int,","                                      comment_id: int,","                                      reaction_type: str):","        pass","","    @abstractmethod","    def update_comment_reaction(self, user_id: int,","                                comment_id: int,","                                reaction_type: str):","        pass","","    @abstractmethod","    def is_comment_reaction_existed(self, user_id: int,","                                    comment_id: int) -> bool:","        pass","","    @abstractmethod","    def get_total_reaction_count(self) -> int:","        pass","","    @abstractmethod","    def can_user_delete_post(self, user_id: int, post_id: int) -> bool:","        pass","","    @abstractmethod","    def delete_post(self, user_id: int, post_id: int):","        pass","","    @abstractmethod","    def get_posts_with_more_positive_reactions(self) -> List[int]:","        pass","","    @abstractmethod","    def get_posts_reacted_by_user(self) -> List[int]:","        pass",""],"id":3},{"start":{"row":32,"column":0},"end":{"row":33,"column":0},"action":"remove","lines":["",""]},{"start":{"row":31,"column":12},"end":{"row":32,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":31,"column":12},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":32,"column":0},"end":{"row":32,"column":8},"action":"insert","lines":["        "]},{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":38,"column":0},"end":{"row":50,"column":0},"action":"remove","lines":["    @abstractmethod","    def get_reaction_metrics_dto(self,","                                 post_id: int) -> List[ReactionMetricsDto]:","        pass","","    @abstractmethod","    def get_post_dto(self, post_id: int) -> PostCompleteDetailsDto:","        pass","","    @abstractmethod","    def get_user_posts_dto(self, user_id: int) -> UserPostsCompleteDetailsDto:","        pass",""],"id":6},{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":37,"column":0},"end":{"row":37,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1590246787618,"hash":"12d49224ca0acf0e06ec68f294752ca0b985a5ca"}