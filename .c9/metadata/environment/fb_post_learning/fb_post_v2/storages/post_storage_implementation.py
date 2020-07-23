{"changed":true,"filter":false,"title":"post_storage_implementation.py","tooltip":"/fb_post_learning/fb_post_v2/storages/post_storage_implementation.py","value":"from abc import ABC\nfrom abc import abstractmethod\nfrom typing import Optional, List\nfrom django.db.models import Count, Q, F, Prefetch\nfrom fb_post_v2.interactors.storages.dtos import *\nfrom fb_post_v2.interactors.storages.post_storage_interface import StorageInterface\nfrom fb_post_v2.models import Post, Comment, Reaction\n\nclass StorageImplementation(StorageInterface):\n    def create_post(self, user_id: int, post_content: str) ->int:\n        post = Post.objects.create(posted_by_id=user_id,\n                                   content=post_content)\n        post_id = post.id\n        return post_id\n\n    def is_valid_post_id(self, post_id: int) -> bool:\n        try:\n            Post.objects.get(id=post_id)\n        except Post.DoesNotExist:\n            return False\n        return True\n\n\n    def can_user_delete_post(self, user_id: int, post_id: int) -> bool:\n        try:\n            Post.objects.get(id=post_id, posted_by_id=user_id)\n        except Post.DoesNotExist:\n            return False\n        return True\n\n    def delete_post(self, user_id: int, post_id: int):\n        Post.objects.get(id=post_id, posted_by_id=user_id).delete()\n        return\n\n    def get_post_dto(self, post_id: int) -> PostCompleteDetailsDto:\n        prefetch_reactions = Prefetch('reactions',\n                                      queryset=Reaction.objects.filter(\n                                          post_id=post_id))\n        prefetch_comments = Prefetch(\n            'comments', queryset=Comment.objects.select_related('commented_by').\n                prefetch_related(Prefetch('reactions')).\n                prefetch_related('parent_comment__commented_by').\n                prefetch_related('parent_comment__reactions')\n        )\n\n        post = Post.objects.select_related('user').prefetch_related(\n            prefetch_reactions, prefetch_comments).get(id=post_id)\n\n        post_details_dto_obj = self._get_post_details_dto_obj(post)\n\n        return post_details_dto_obj\n\n\n    def get_user_posts_dto(self, user_id: int) -> UserPostsCompleteDetailsDto:\n        prefetch_reactions = Prefetch('reactions',\n                                      queryset=Reaction.objects.filter(\n                                          post_id=post_id))\n        prefetch_comments = Prefetch(\n            'comments', queryset=Comment.objects.select_related('commented_by').\n                prefetch_related(Prefetch('reactions')).\n                prefetch_related('parent_comment__commented_by').\n                prefetch_related('parent_comment__reactions')\n        )\n\n        posts = Post.objects.select_related('posted_by').prefetch_related(\n            prefetch_reactions, prefetch_comments).get(posted_by_id=user_id)\n\n        list_of_posts_details_dtos_obj = self._get_posts_details_dtos_obj(posts)\n        return list_of_posts_details_dtos_obj\n\n    def _get_post_details_dto_obj(self, post):\n        post_user_dto_dict = {}\n        reaction_dtos = []\n        post_dto = self._convert_post_obj_to_dto(post)\n        post_reaction_dtos = self._get_object_reactions(post)\n        posted_user = post.posted_by\n\n        user_dto = self._convert_user_object_to_dto(posted_user)\n        user_id = user_dto.user_id\n        post_user_dto_dict[user_id] = user_dto\n        comments = post.comments.all()\n        users_dto_dict, comment_dtos, comment_reaction_dtos = \\\n            self._get_comments_details(comments)\n\n        reply_dtos, reply_reaction_dtos = self._get_replies_details(comments)\n\n        reaction_dtos += post_reaction_dtos\n        reaction_dtos += comment_reaction_dtos\n        reaction_dtos += reply_reaction_dtos\n        comment_dtos += reply_dtos\n\n        users_dto_dict.update(post_user_dto_dict)\n        \n        user_dtos = list(users_dto_dict.values())\n        post_details_dto = PostCompleteDetailsDto(post_dto=post_dto,\n                                                  reactions_dto=reaction_dtos,\n                                                  comments_dto=comment_dtos,\n                                                  users_dto=user_dtos)\n        return post_details_dto\n\n    def _get_posts_details_dtos_obj(self, posts):\n        post_user_dto_dict = {}\n        reaction_dtos, post_reaction_dtos, user_dto = [], [], []\n        posts_dto, comments = [], []\n        for post in posts:\n            posts_dto += self._convert_post_obj_to_dto(post)\n            post_reaction_dtos += self._get_object_reactions(posts)\n            posted_user = post.posted_by\n\n            user_dto = self._convert_user_object_to_dto(posted_user)\n            user_id = user_dto.user_id\n            post_user_dto_dict[user_id] = user_dto\n            comments += post.comments.all()\n        users_dto_dict, comment_dtos, comment_reaction_dtos = \\\n            self._get_comments_details(comments)\n\n        reply_dtos, reply_reaction_dtos = self._get_replies_details(comments)\n\n        reaction_dtos += post_reaction_dtos\n        reaction_dtos += comment_reaction_dtos\n        reaction_dtos += reply_reaction_dtos\n        comment_dtos += reply_dtos\n\n        users_dto_dict.update(post_user_dto_dict)\n        \n        user_dtos = list(users_dto_dict.values())\n        user_posts_details_dto = PostCompleteDetailsDto(post_dto=post_dto,\n                                                  reactions_dto=reaction_dtos,\n                                                  comments_dto=comment_dtos,\n                                                  users_dto=user_dtos)\n        return user_posts_details_dto\n\n    def _convert_post_obj_to_dto(self, post):\n        post_dto = PostDto(\n            user_id=post.posted_by_id,\n            post_content=post.content,\n            post_id= post.id,\n            pub_date_time=post.posted_at\n        )\n        return post_dto\n\n    def _get_reactions(self, list_of_objects):\n        reaction_dtos = []\n        for object in list_of_objects:\n            object_reaction_dtos = self._get_object_reactions(object)\n            reaction_dtos += object_reaction_dtos\n        return reaction_dtos\n\n    def _get_object_reactions(self, object):\n        reaction_dtos = []\n        reactions = object.reactions.all()\n        for reaction in reactions:\n            reaction_dto = self._convert_reaction_object_to_dto(reaction)\n            reaction_dtos.append(reaction_dto)\n        return reaction_dtos\n\n    def _convert_comment_obj_to_dto(self, comment):\n        comment_dto = CommentDto(\n            comment_id=comment.id,\n            user_id=comment.user.id,\n            post_id=comment.post.id,\n            comment_content=comment.comment_text,\n            pub_date_time=comment.pub_date_time.replace(tzinfo=None),\n            parent_comment=comment.parent_comment)\n        return comment_dto\n\n    def _convert_reaction_object_to_dto(self, reaction):\n        reaction_dto = ReactionDto(\n            reaction_id=reaction.id,\n            comment_id=reaction.comment_id,\n            post_id=reaction.post_id,\n            user_id=reaction.reacted_by_id,\n            reaction_type=reaction.reaction\n        )\n        return reaction_dto\n\n    def _get_comments_details(self, comments):\n        users_dto_dict = {}\n        comments_dtos = []\n        comments_reaction_dtos = []\n\n        for comment in comments:\n            users_dto_dict, comment_dto, comment_reaction_dto = \\\n                self._get_comment_details(comment)\n            comments_dtos += comment_dto\n            comments_reaction_dtos += comment_reaction_dto\n            users_dto_dict.update(users_dto_dict)\n\n        return users_dto_dict, comments_dtos, comments_reaction_dtos\n\n    def _get_comment_details(self, comment):\n        users_dto_dict = {}\n        comment_dtos = []\n        comment_dto = self._convert_comment_obj_to_dto(comment)\n        comment_dtos.append(comment_dto)\n        comment_user = comment.commented_by\n\n        user_dto = self._convert_user_object_to_dto(comment_user)\n        user_id = user_dto.user_id\n        users_dto_dict[user_id] = user_dto\n\n        comment_reaction_dtos = self._get_reactions(\n            comment)\n\n        return users_dto_dict, comment_dtos, comment_reaction_dtos\n\n    def _get_replies_details(self, comments):\n        reply_dtos = []\n        reply_reaction_dtos = []\n\n        for comment in comments:\n            comment_dto, comment_reaction_dto = self._get_reply_details(comment)\n            reply_dtos += comment_dto\n            reply_reaction_dtos += comment_reaction_dto\n\n        return reply_dtos, reply_reaction_dtos\n\n    def _get_reply_details(self, comment):\n        users_dto_dict = {}\n        reply_dtos = []\n        reply_reaction_dtos = []\n        replies = comment.comments.all()\n        for reply in replies:\n            reply_dto = self._convert_comment_obj_to_dto(reply)\n            reply_dtos.append(reply_dto)\n\n        reply_reaction_dtos += self._get_reactions(replies)\n        for reply in replies:\n            user = reply.commented_by\n            user_dto = self._convert_user_object_to_dto(user)\n            user_id = user_dto.user_id\n            users_dto_dict[user_id] = user_dto\n        return reply_dtos, reply_reaction_dtos\n\n    def _convert_user_object_to_dto(self, user):\n        user_dto = UserDto(\n            user_id=user.id,\n            name=user.name,\n            profile_pic=user.profile_pic\n        )\n        return user_dto","undoManager":{"mark":-4,"position":100,"stack":[[{"start":{"row":275,"column":25},"end":{"row":275,"column":26},"action":"remove","lines":["s"],"id":53}],[{"start":{"row":275,"column":8},"end":{"row":275,"column":9},"action":"insert","lines":["u"],"id":54},{"start":{"row":275,"column":9},"end":{"row":275,"column":10},"action":"insert","lines":["s"]},{"start":{"row":275,"column":10},"end":{"row":275,"column":11},"action":"insert","lines":["e"]},{"start":{"row":275,"column":11},"end":{"row":275,"column":12},"action":"insert","lines":["r"]},{"start":{"row":275,"column":12},"end":{"row":275,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":279,"column":32},"end":{"row":279,"column":33},"action":"remove","lines":["s"],"id":55}],[{"start":{"row":279,"column":15},"end":{"row":279,"column":16},"action":"insert","lines":["u"],"id":56},{"start":{"row":279,"column":16},"end":{"row":279,"column":17},"action":"insert","lines":["s"]},{"start":{"row":279,"column":17},"end":{"row":279,"column":18},"action":"insert","lines":["e"]},{"start":{"row":279,"column":18},"end":{"row":279,"column":19},"action":"insert","lines":["r"]},{"start":{"row":279,"column":19},"end":{"row":279,"column":20},"action":"insert","lines":["_"]}],[{"start":{"row":251,"column":17},"end":{"row":251,"column":18},"action":"insert","lines":["s"],"id":57}],[{"start":{"row":251,"column":30},"end":{"row":251,"column":31},"action":"insert","lines":["s"],"id":58}],[{"start":{"row":251,"column":42},"end":{"row":251,"column":43},"action":"insert","lines":["l"],"id":59},{"start":{"row":251,"column":43},"end":{"row":251,"column":44},"action":"insert","lines":["i"]},{"start":{"row":251,"column":44},"end":{"row":251,"column":45},"action":"insert","lines":["s"]},{"start":{"row":251,"column":45},"end":{"row":251,"column":46},"action":"insert","lines":["t"]}],[{"start":{"row":251,"column":46},"end":{"row":251,"column":47},"action":"insert","lines":["_"],"id":60}],[{"start":{"row":251,"column":47},"end":{"row":251,"column":48},"action":"insert","lines":["o"],"id":61},{"start":{"row":251,"column":48},"end":{"row":251,"column":49},"action":"insert","lines":["f"]},{"start":{"row":251,"column":49},"end":{"row":251,"column":50},"action":"insert","lines":["_"]}],[{"start":{"row":219,"column":11},"end":{"row":219,"column":12},"action":"remove","lines":["s"],"id":62},{"start":{"row":219,"column":10},"end":{"row":219,"column":11},"action":"remove","lines":["s"]},{"start":{"row":219,"column":9},"end":{"row":219,"column":10},"action":"remove","lines":["a"]},{"start":{"row":219,"column":8},"end":{"row":219,"column":9},"action":"remove","lines":["p"]}],[{"start":{"row":219,"column":8},"end":{"row":219,"column":67},"action":"insert","lines":["post_details_dto_obj = self._get_post_details_dto_obj(post)"],"id":63}],[{"start":{"row":218,"column":76},"end":{"row":219,"column":0},"action":"insert","lines":["",""],"id":64},{"start":{"row":219,"column":0},"end":{"row":219,"column":12},"action":"insert","lines":["            "]},{"start":{"row":219,"column":12},"end":{"row":219,"column":13},"action":"insert","lines":["\\"]}],[{"start":{"row":219,"column":12},"end":{"row":219,"column":13},"action":"remove","lines":["\\"],"id":65},{"start":{"row":219,"column":8},"end":{"row":219,"column":12},"action":"remove","lines":["    "]},{"start":{"row":219,"column":4},"end":{"row":219,"column":8},"action":"remove","lines":["    "]},{"start":{"row":219,"column":0},"end":{"row":219,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":220,"column":66},"end":{"row":220,"column":67},"action":"insert","lines":["s"],"id":66}],[{"start":{"row":220,"column":57},"end":{"row":220,"column":58},"action":"insert","lines":["s"],"id":67}],[{"start":{"row":220,"column":45},"end":{"row":220,"column":46},"action":"insert","lines":["s"],"id":68}],[{"start":{"row":220,"column":70},"end":{"row":221,"column":0},"action":"insert","lines":["",""],"id":69},{"start":{"row":221,"column":0},"end":{"row":221,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":221,"column":4},"end":{"row":221,"column":8},"action":"remove","lines":["    "],"id":70}],[{"start":{"row":221,"column":4},"end":{"row":221,"column":8},"action":"insert","lines":["    "],"id":71}],[{"start":{"row":221,"column":8},"end":{"row":221,"column":35},"action":"insert","lines":["return post_details_dto_obj"],"id":72}],[{"start":{"row":220,"column":8},"end":{"row":220,"column":9},"action":"insert","lines":["l"],"id":73},{"start":{"row":220,"column":9},"end":{"row":220,"column":10},"action":"insert","lines":["i"]},{"start":{"row":220,"column":10},"end":{"row":220,"column":11},"action":"insert","lines":["s"]},{"start":{"row":220,"column":11},"end":{"row":220,"column":12},"action":"insert","lines":["t"]},{"start":{"row":220,"column":12},"end":{"row":220,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":220,"column":13},"end":{"row":220,"column":14},"action":"insert","lines":["o"],"id":74},{"start":{"row":220,"column":14},"end":{"row":220,"column":15},"action":"insert","lines":["f"]},{"start":{"row":220,"column":15},"end":{"row":220,"column":16},"action":"insert","lines":["_"]}],[{"start":{"row":220,"column":20},"end":{"row":220,"column":21},"action":"insert","lines":["s"],"id":75}],[{"start":{"row":220,"column":33},"end":{"row":220,"column":34},"action":"insert","lines":["s"],"id":76}],[{"start":{"row":221,"column":15},"end":{"row":221,"column":35},"action":"remove","lines":["post_details_dto_obj"],"id":77},{"start":{"row":221,"column":15},"end":{"row":221,"column":45},"action":"insert","lines":["list_of_posts_details_dtos_obj"]}],[{"start":{"row":256,"column":12},"end":{"row":256,"column":13},"action":"insert","lines":["s"],"id":78}],[{"start":{"row":253,"column":49},"end":{"row":253,"column":50},"action":"remove","lines":["_"],"id":79},{"start":{"row":253,"column":48},"end":{"row":253,"column":49},"action":"remove","lines":["f"]},{"start":{"row":253,"column":47},"end":{"row":253,"column":48},"action":"remove","lines":["o"]},{"start":{"row":253,"column":46},"end":{"row":253,"column":47},"action":"remove","lines":["_"]},{"start":{"row":253,"column":45},"end":{"row":253,"column":46},"action":"remove","lines":["t"]},{"start":{"row":253,"column":44},"end":{"row":253,"column":45},"action":"remove","lines":["s"]},{"start":{"row":253,"column":43},"end":{"row":253,"column":44},"action":"remove","lines":["i"]},{"start":{"row":253,"column":42},"end":{"row":253,"column":43},"action":"remove","lines":["l"]}],[{"start":{"row":253,"column":46},"end":{"row":253,"column":47},"action":"insert","lines":["s"],"id":80}],[{"start":{"row":256,"column":50},"end":{"row":256,"column":54},"action":"remove","lines":["post"],"id":81},{"start":{"row":256,"column":50},"end":{"row":256,"column":55},"action":"insert","lines":["posts"]}],[{"start":{"row":257,"column":56},"end":{"row":257,"column":60},"action":"remove","lines":["post"],"id":82},{"start":{"row":257,"column":56},"end":{"row":257,"column":61},"action":"insert","lines":["posts"]}],[{"start":{"row":255,"column":26},"end":{"row":256,"column":0},"action":"insert","lines":["",""],"id":83},{"start":{"row":256,"column":0},"end":{"row":256,"column":8},"action":"insert","lines":["        "]},{"start":{"row":256,"column":8},"end":{"row":256,"column":9},"action":"insert","lines":["f"]},{"start":{"row":256,"column":9},"end":{"row":256,"column":10},"action":"insert","lines":["o"]},{"start":{"row":256,"column":10},"end":{"row":256,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":256,"column":11},"end":{"row":256,"column":12},"action":"insert","lines":[" "],"id":84}],[{"start":{"row":255,"column":26},"end":{"row":256,"column":0},"action":"insert","lines":["",""],"id":85},{"start":{"row":256,"column":0},"end":{"row":256,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":256,"column":8},"end":{"row":256,"column":17},"action":"insert","lines":["posts_dto"],"id":86}],[{"start":{"row":256,"column":17},"end":{"row":256,"column":18},"action":"insert","lines":[" "],"id":87},{"start":{"row":256,"column":18},"end":{"row":256,"column":19},"action":"insert","lines":["="]}],[{"start":{"row":256,"column":19},"end":{"row":256,"column":20},"action":"insert","lines":[" "],"id":88}],[{"start":{"row":256,"column":20},"end":{"row":256,"column":22},"action":"insert","lines":["[]"],"id":89}],[{"start":{"row":257,"column":12},"end":{"row":257,"column":13},"action":"insert","lines":["p"],"id":90},{"start":{"row":257,"column":13},"end":{"row":257,"column":14},"action":"insert","lines":["o"]},{"start":{"row":257,"column":14},"end":{"row":257,"column":15},"action":"insert","lines":["s"]},{"start":{"row":257,"column":15},"end":{"row":257,"column":16},"action":"insert","lines":["t"]},{"start":{"row":257,"column":16},"end":{"row":257,"column":17},"action":"insert","lines":[")"]}],[{"start":{"row":257,"column":16},"end":{"row":257,"column":17},"action":"remove","lines":[")"],"id":91}],[{"start":{"row":257,"column":16},"end":{"row":257,"column":17},"action":"insert","lines":["_"],"id":92},{"start":{"row":257,"column":17},"end":{"row":257,"column":18},"action":"insert","lines":["i"]}],[{"start":{"row":257,"column":17},"end":{"row":257,"column":18},"action":"remove","lines":["i"],"id":93},{"start":{"row":257,"column":16},"end":{"row":257,"column":17},"action":"remove","lines":["_"]}],[{"start":{"row":257,"column":16},"end":{"row":257,"column":17},"action":"insert","lines":[" "],"id":94},{"start":{"row":257,"column":17},"end":{"row":257,"column":18},"action":"insert","lines":["i"]},{"start":{"row":257,"column":18},"end":{"row":257,"column":19},"action":"insert","lines":["n"]}],[{"start":{"row":257,"column":19},"end":{"row":257,"column":20},"action":"insert","lines":[" "],"id":95},{"start":{"row":257,"column":20},"end":{"row":257,"column":21},"action":"insert","lines":["p"]},{"start":{"row":257,"column":21},"end":{"row":257,"column":22},"action":"insert","lines":["o"]},{"start":{"row":257,"column":22},"end":{"row":257,"column":23},"action":"insert","lines":["s"]},{"start":{"row":257,"column":23},"end":{"row":257,"column":24},"action":"insert","lines":["t"]},{"start":{"row":257,"column":24},"end":{"row":257,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":257,"column":24},"end":{"row":257,"column":25},"action":"remove","lines":["e"],"id":96}],[{"start":{"row":257,"column":24},"end":{"row":257,"column":25},"action":"insert","lines":["s"],"id":97},{"start":{"row":257,"column":25},"end":{"row":257,"column":26},"action":"insert","lines":[":"]}],[{"start":{"row":257,"column":26},"end":{"row":258,"column":0},"action":"insert","lines":["",""],"id":98},{"start":{"row":258,"column":0},"end":{"row":258,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":258,"column":12},"end":{"row":258,"column":21},"action":"insert","lines":["posts_dto"],"id":99}],[{"start":{"row":258,"column":20},"end":{"row":258,"column":21},"action":"remove","lines":["o"],"id":100},{"start":{"row":258,"column":19},"end":{"row":258,"column":20},"action":"remove","lines":["t"]},{"start":{"row":258,"column":18},"end":{"row":258,"column":19},"action":"remove","lines":["d"]},{"start":{"row":258,"column":17},"end":{"row":258,"column":18},"action":"remove","lines":["_"]},{"start":{"row":258,"column":16},"end":{"row":258,"column":17},"action":"remove","lines":["s"]},{"start":{"row":258,"column":15},"end":{"row":258,"column":16},"action":"remove","lines":["t"]},{"start":{"row":258,"column":14},"end":{"row":258,"column":15},"action":"remove","lines":["s"]},{"start":{"row":258,"column":13},"end":{"row":258,"column":14},"action":"remove","lines":["o"]},{"start":{"row":258,"column":12},"end":{"row":258,"column":13},"action":"remove","lines":["p"]}],[{"start":{"row":259,"column":4},"end":{"row":259,"column":8},"action":"remove","lines":["    "],"id":101},{"start":{"row":259,"column":0},"end":{"row":259,"column":4},"action":"remove","lines":["    "]},{"start":{"row":258,"column":12},"end":{"row":259,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":258,"column":22},"end":{"row":258,"column":23},"action":"insert","lines":["+"],"id":102}],[{"start":{"row":258,"column":59},"end":{"row":258,"column":60},"action":"remove","lines":["s"],"id":103}],[{"start":{"row":255,"column":21},"end":{"row":255,"column":22},"action":"insert","lines":[","],"id":104}],[{"start":{"row":255,"column":22},"end":{"row":255,"column":23},"action":"insert","lines":[" "],"id":105}],[{"start":{"row":255,"column":23},"end":{"row":255,"column":41},"action":"insert","lines":["post_reaction_dtos"],"id":106}],[{"start":{"row":255,"column":46},"end":{"row":255,"column":47},"action":"insert","lines":[","],"id":107}],[{"start":{"row":255,"column":47},"end":{"row":255,"column":48},"action":"insert","lines":[" "],"id":108}],[{"start":{"row":255,"column":48},"end":{"row":255,"column":50},"action":"insert","lines":["[]"],"id":109}],[{"start":{"row":259,"column":27},"end":{"row":259,"column":28},"action":"insert","lines":["+"],"id":110}],[{"start":{"row":258,"column":60},"end":{"row":259,"column":0},"action":"insert","lines":["",""],"id":111},{"start":{"row":259,"column":0},"end":{"row":259,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":259,"column":8},"end":{"row":259,"column":12},"action":"remove","lines":["    "],"id":112}],[{"start":{"row":259,"column":8},"end":{"row":259,"column":9},"action":"insert","lines":["f"],"id":113},{"start":{"row":259,"column":9},"end":{"row":259,"column":10},"action":"insert","lines":["o"]},{"start":{"row":259,"column":10},"end":{"row":259,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":259,"column":11},"end":{"row":259,"column":12},"action":"insert","lines":[" "],"id":114}],[{"start":{"row":259,"column":12},"end":{"row":259,"column":13},"action":"insert","lines":["p"],"id":115},{"start":{"row":259,"column":13},"end":{"row":259,"column":14},"action":"insert","lines":["o"]},{"start":{"row":259,"column":14},"end":{"row":259,"column":15},"action":"insert","lines":["s"]},{"start":{"row":259,"column":15},"end":{"row":259,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":259,"column":16},"end":{"row":259,"column":17},"action":"insert","lines":[" "],"id":116},{"start":{"row":259,"column":17},"end":{"row":259,"column":18},"action":"insert","lines":["i"]},{"start":{"row":259,"column":18},"end":{"row":259,"column":19},"action":"insert","lines":["n"]}],[{"start":{"row":259,"column":19},"end":{"row":259,"column":20},"action":"insert","lines":[" "],"id":117},{"start":{"row":259,"column":20},"end":{"row":259,"column":21},"action":"insert","lines":["p"]},{"start":{"row":259,"column":21},"end":{"row":259,"column":22},"action":"insert","lines":["o"]},{"start":{"row":259,"column":22},"end":{"row":259,"column":23},"action":"insert","lines":["s"]},{"start":{"row":259,"column":23},"end":{"row":259,"column":24},"action":"insert","lines":["t"]},{"start":{"row":259,"column":24},"end":{"row":259,"column":25},"action":"insert","lines":["s"]},{"start":{"row":259,"column":25},"end":{"row":259,"column":26},"action":"insert","lines":[":"]}],[{"start":{"row":260,"column":8},"end":{"row":260,"column":12},"action":"insert","lines":["    "],"id":118}],[{"start":{"row":255,"column":41},"end":{"row":255,"column":42},"action":"insert","lines":[","],"id":119}],[{"start":{"row":255,"column":42},"end":{"row":255,"column":43},"action":"insert","lines":[" "],"id":120},{"start":{"row":255,"column":43},"end":{"row":255,"column":44},"action":"insert","lines":["u"]},{"start":{"row":255,"column":44},"end":{"row":255,"column":45},"action":"insert","lines":["s"]},{"start":{"row":255,"column":45},"end":{"row":255,"column":46},"action":"insert","lines":["e"]},{"start":{"row":255,"column":46},"end":{"row":255,"column":47},"action":"insert","lines":["r"]}],[{"start":{"row":255,"column":47},"end":{"row":255,"column":48},"action":"insert","lines":["_"],"id":121},{"start":{"row":255,"column":48},"end":{"row":255,"column":49},"action":"insert","lines":["d"]},{"start":{"row":255,"column":49},"end":{"row":255,"column":50},"action":"insert","lines":["t"]},{"start":{"row":255,"column":50},"end":{"row":255,"column":51},"action":"insert","lines":["o"]}],[{"start":{"row":255,"column":60},"end":{"row":255,"column":61},"action":"insert","lines":[","],"id":122}],[{"start":{"row":255,"column":61},"end":{"row":255,"column":62},"action":"insert","lines":[" "],"id":123}],[{"start":{"row":255,"column":62},"end":{"row":255,"column":64},"action":"insert","lines":["[]"],"id":124}],[{"start":{"row":261,"column":8},"end":{"row":261,"column":12},"action":"insert","lines":["    "],"id":125}],[{"start":{"row":259,"column":0},"end":{"row":259,"column":26},"action":"remove","lines":["        for post in posts:"],"id":126},{"start":{"row":258,"column":60},"end":{"row":259,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":262,"column":8},"end":{"row":262,"column":12},"action":"insert","lines":["    "],"id":127}],[{"start":{"row":262,"column":21},"end":{"row":262,"column":22},"action":"insert","lines":["+"],"id":128}],[{"start":{"row":263,"column":8},"end":{"row":263,"column":12},"action":"insert","lines":["    "],"id":129}],[{"start":{"row":264,"column":8},"end":{"row":264,"column":12},"action":"insert","lines":["    "],"id":130}],[{"start":{"row":265,"column":8},"end":{"row":265,"column":12},"action":"insert","lines":["    "],"id":131}],[{"start":{"row":256,"column":17},"end":{"row":256,"column":18},"action":"insert","lines":[","],"id":132}],[{"start":{"row":256,"column":18},"end":{"row":256,"column":19},"action":"insert","lines":[" "],"id":133},{"start":{"row":256,"column":19},"end":{"row":256,"column":20},"action":"insert","lines":["c"]},{"start":{"row":256,"column":20},"end":{"row":256,"column":21},"action":"insert","lines":["o"]},{"start":{"row":256,"column":21},"end":{"row":256,"column":22},"action":"insert","lines":["m"]},{"start":{"row":256,"column":22},"end":{"row":256,"column":23},"action":"insert","lines":["m"]},{"start":{"row":256,"column":23},"end":{"row":256,"column":24},"action":"insert","lines":["e"]},{"start":{"row":256,"column":24},"end":{"row":256,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":256,"column":25},"end":{"row":256,"column":26},"action":"insert","lines":["t"],"id":134},{"start":{"row":256,"column":26},"end":{"row":256,"column":27},"action":"insert","lines":["s"]}],[{"start":{"row":256,"column":32},"end":{"row":256,"column":33},"action":"insert","lines":[","],"id":135}],[{"start":{"row":256,"column":33},"end":{"row":256,"column":34},"action":"insert","lines":[" "],"id":136}],[{"start":{"row":256,"column":34},"end":{"row":256,"column":36},"action":"insert","lines":["[]"],"id":137}],[{"start":{"row":265,"column":21},"end":{"row":265,"column":22},"action":"insert","lines":["+"],"id":138}],[{"start":{"row":262,"column":21},"end":{"row":262,"column":22},"action":"remove","lines":["+"],"id":139}],[{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":["p"],"id":140},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"insert","lines":["o"]},{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"insert","lines":["s"]},{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"insert","lines":["t"]},{"start":{"row":5,"column":41},"end":{"row":5,"column":42},"action":"insert","lines":["_"]}],[{"start":{"row":15,"column":4},"end":{"row":22,"column":0},"action":"remove","lines":["def create_comment(self, user_id: int, post_id: int,","                       comment_content: str) ->int:","        comment = Comment.objects.create(commented_by_id=user_id,","                                         post_id=post_id,","                                         content=comment_content)","        comment_id = comment.id","        return comment_id",""],"id":141},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":22,"column":0},"end":{"row":116,"column":0},"action":"remove","lines":["","    def is_valid_comment_id(self, comment_id: int) -> bool:","        try:","            Comment.objects.get(id=comment_id)","        except Comment.DoesNotExist:","            return False","        return True","","    def reply_to_comment(self, user_id: int, comment_id: int,","                         reply_content: str) ->int:","        comment = Comment.objects.get(id=comment_id)","        post_id = comment.post_id","        reply = Comment.objects.create(commented_by_id=user_id,","                                       post_id=post_id,","                                       parent_comment_id=comment_id,","                                       content=reply_content)","        reply_id = reply.id","        return reply_id","","","    def is_reply(self, comment_id: int) -> bool:","        comment = Comment.objects.get(id=comment_id)","        is_comment_is_reply_comment = comment.parent_comment_id","        if is_comment_is_reply_comment:","            return True","        return False","","    def get_parent_comment_id(self, reply_id: int) -> int:","        parent_comment = Comment.objects.get(id=reply_id)","        parent_comment_id = parent_comment.id","        return parent_comment_id","","    def react_to_post(self, user_id: int, post_id: int, reaction_type: str):","        Reaction.objects.create(user_id=user_id,","                                 post_id=post_id,","                                 reaction_type=reaction_type)","","    def make_undo_to_post_reaction(self, user_id: int,","                                   post_id: int,","                                   reaction_type: str):","        Reaction.objects.get(user_id=user_id,","                              post_id=post_id).delete()","","    def update_post_reaction(self, user_id: int,","                             post_id: int,","                             reaction_type: str):","        Reaction.objects.filter(user_id=user_id,","                                 post_id=post_id).update(","            reaction_type=reaction_type)","","    def is_reaction_type_existed(self, reaction_type: str) -> bool:","        pass","","    def is_post_reaction_existed(self, user_id: int, post_id: int) -> bool:","        try:","            Reaction.objects.get(reacted_by_id=user_id, post_id=post_id)","        except Reaction.DoesNotExist:","            return False","        return True","","    def is_reaction_type_valid(self, reaction_type: str) -> bool:","        pass","","    def react_to_comment(self, user_id: int,","                         comment_id: int,","                         reaction_type: str):","        Reaction.objects.create(user_id=user_id,","                                 comment_id=comment_id,","                                 reaction_type=reaction_type)","","    def make_undo_to_comment_reaction(self, user_id: int,","                                      comment_id: int,","                                      reaction_type: str):","        Reaction.objects.get(user_id=user_id,","                              comment_id=comment_id).delete()","","    def update_comment_reaction(self, user_id: int,","                                comment_id: int,","                                reaction_type: str):","        Reaction.objects.filter(user_id=user_id,","                                 comment_id=comment_id).update(","            reaction_type=reaction_type)","","    def is_comment_reaction_existed(self, user_id: int,","                                    comment_id: int) -> bool:","        try:","            Reaction.objects.get(reacted_by_id=user_id, comment_id=comment_id)","        except Reaction.DoesNotExist:","            return False","        return True","","    def get_total_reaction_count(self) -> int:","        total_reaction_count = Reaction.objects.aggregate(count=Count('id'))","        return total_reaction_count",""],"id":142}],[{"start":{"row":33,"column":0},"end":{"row":85,"column":0},"action":"remove","lines":["","    def get_posts_with_more_positive_reactions(self) -> List[int]:","        positive_reactions = [ReactionType.THUMBS_UP.value,","                              ReactionType.LIT.value,","                              ReactionType.WOW.value,","                              ReactionType.HAHA.value,","                              ReactionType.LOVE.value]","        negative_reactions = [ReactionType.THUMBS_DOWN.value,","                              ReactionType.SAD.value,","                              ReactionType.ANGRY.value]","","        positive_reactions_count = Count('reaction', filter=Q(","            reaction__in=positive_reactions))","        negative_reactions_count = Count('reaction', filter=Q(","            reaction__in=negative_reactions))","","        post_ids = Reaction.objects.filter(comment_id__isnull=True).values('post').\\","                    annotate(","                        positive_count=positive_reactions_count,","                        negative_count=negative_reactions_count","                    ).filter(","                        positive_count__gt=F('negative_count')","                    ).values_list(","                        'post_id', flat=True","                    ).distinct()","        post_ids_list = list(post_ids)","        return post_ids_list","","    def get_posts_reacted_by_user(self, user_id) -> List[int]:","        post_ids = Reaction.objects.filter(","                reacted_by__id=user_id,","                comment_id__isnull=True","                ).values_list(","                    'post_id', flat=True","                ).distinct()","        post_ids_list = list(post_ids)","        return post_ids_list","","    def get_replies_for_comment_dto(self,","                                    comment_id: int) -> List[CommentRepliesDto]:","        pass","","    def get_reaction_metrics_dto(self,","                                 post_id: int) -> List[ReactionMetricsDto]:","        reaction = Reaction.objects.filter(post_id=post_id).values('reaction').\\","                    annotate(","                        count=Count('reaction')","                    ).values_list('reaction', 'count')","","        reaction_metrics_dict = dict(reaction)","        return reaction_metrics_dict","",""],"id":143}],[{"start":{"row":32,"column":14},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":144},{"start":{"row":33,"column":0},"end":{"row":33,"column":8},"action":"insert","lines":["        "]},{"start":{"row":33,"column":4},"end":{"row":33,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "],"id":145}],[{"start":{"row":212,"column":12},"end":{"row":212,"column":16},"action":"remove","lines":["    "],"id":146},{"start":{"row":212,"column":8},"end":{"row":212,"column":12},"action":"remove","lines":["    "]},{"start":{"row":212,"column":4},"end":{"row":212,"column":8},"action":"remove","lines":["    "]},{"start":{"row":212,"column":0},"end":{"row":212,"column":4},"action":"remove","lines":["    "]},{"start":{"row":211,"column":72},"end":{"row":212,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":165,"column":0},"end":{"row":166,"column":0},"action":"insert","lines":["",""],"id":147}],[{"start":{"row":165,"column":0},"end":{"row":166,"column":0},"action":"remove","lines":["",""],"id":148}],[{"start":{"row":64,"column":48},"end":{"row":64,"column":49},"action":"remove","lines":["r"],"id":149},{"start":{"row":64,"column":47},"end":{"row":64,"column":48},"action":"remove","lines":["e"]},{"start":{"row":64,"column":46},"end":{"row":64,"column":47},"action":"remove","lines":["s"]},{"start":{"row":64,"column":45},"end":{"row":64,"column":46},"action":"remove","lines":["u"]}],[{"start":{"row":64,"column":45},"end":{"row":64,"column":46},"action":"insert","lines":["p"],"id":150},{"start":{"row":64,"column":46},"end":{"row":64,"column":47},"action":"insert","lines":["o"]},{"start":{"row":64,"column":47},"end":{"row":64,"column":48},"action":"insert","lines":["s"]},{"start":{"row":64,"column":48},"end":{"row":64,"column":49},"action":"insert","lines":["t"]},{"start":{"row":64,"column":49},"end":{"row":64,"column":50},"action":"insert","lines":["e"]},{"start":{"row":64,"column":50},"end":{"row":64,"column":51},"action":"insert","lines":["d"]},{"start":{"row":64,"column":51},"end":{"row":64,"column":52},"action":"insert","lines":["_"]}],[{"start":{"row":64,"column":52},"end":{"row":64,"column":53},"action":"insert","lines":["b"],"id":151},{"start":{"row":64,"column":53},"end":{"row":64,"column":54},"action":"insert","lines":["y"]}],[{"start":{"row":36,"column":47},"end":{"row":36,"column":56},"action":"remove","lines":["Reactions"],"id":152},{"start":{"row":36,"column":47},"end":{"row":36,"column":55},"action":"insert","lines":["Reaction"]}],[{"start":{"row":55,"column":47},"end":{"row":55,"column":56},"action":"remove","lines":["Reactions"],"id":153},{"start":{"row":55,"column":47},"end":{"row":55,"column":55},"action":"insert","lines":["Reaction"]}],[{"start":{"row":57,"column":38},"end":{"row":57,"column":39},"action":"insert","lines":[" "],"id":161}],[{"start":{"row":57,"column":37},"end":{"row":57,"column":38},"action":"insert","lines":["c"],"id":160}]]},"ace":{"folds":[],"scrolltop":823.5,"scrollleft":0,"selection":{"start":{"row":57,"column":37},"end":{"row":57,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":40,"state":"start","mode":"ace/mode/python"}},"timestamp":1593078755557}