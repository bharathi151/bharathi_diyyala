{"filter":false,"title":"tests.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_004/fb_post/tests.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["*"],"id":2}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["U"],"id":3}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["U"],"id":4},{"start":{"row":3,"column":20},"end":{"row":3,"column":24},"action":"insert","lines":["User"]}],[{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":[","],"id":5}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":[" "],"id":6},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["C"]}],[{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":["C"],"id":7},{"start":{"row":3,"column":26},"end":{"row":3,"column":33},"action":"insert","lines":["Comment"]}],[{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":[","],"id":8}],[{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":[" "],"id":9},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["P"]}],[{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"remove","lines":["P"],"id":10},{"start":{"row":3,"column":35},"end":{"row":3,"column":39},"action":"insert","lines":["Post"]}],[{"start":{"row":3,"column":39},"end":{"row":3,"column":40},"action":"insert","lines":[","],"id":11}],[{"start":{"row":3,"column":40},"end":{"row":3,"column":41},"action":"insert","lines":[" "],"id":12},{"start":{"row":3,"column":41},"end":{"row":3,"column":42},"action":"insert","lines":["R"]}],[{"start":{"row":3,"column":41},"end":{"row":3,"column":42},"action":"remove","lines":["R"],"id":13},{"start":{"row":3,"column":41},"end":{"row":3,"column":49},"action":"insert","lines":["Reaction"]}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":13},"action":"remove","lines":["import pytest"],"id":14}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":15}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":13},"action":"insert","lines":["import pytest"],"id":16}],[{"start":{"row":151,"column":0},"end":{"row":215,"column":0},"action":"remove","lines":["@pytest.mark.django_db","def test_create_comment_with_invalid_user_id_raises_InvalidUserException(user,post):","    #arrange","    user_id = 2","    post_id = 1","    comment_content = \"post1_comment1\"","    #act","    with pytest.raises(InvalidUserException) as e:","        assert create_comment(user_id,post_id,comment_content)","    ","    #assert","    user = User.objects.filter(id = user_id)","    ","    assert str(e.value)   ==   \"\"","    assert len(user)   ==   0","    ","    ","@pytest.mark.django_db","def test_create_comment_with_invalid_post_id_raises_InvalidPostException(user,post):","    #arrange","    user_id = 1","    post_id = 3","    comment_content = \"post1_comment1\"","    #act","    with pytest.raises(InvalidPostException) as e:","        assert create_comment(user_id,post_id,comment_content)","    ","    #assert","    post = Post.objects.filter(id = post_id)","    ","    assert str(e.value)   ==   \"\"","    assert len(post)   ==   0","    ","    ","@pytest.mark.django_db","def test_create_comment_with_invalid_comment_content_raises_InvalidCommentContent(user,post):","    user_id = 1","    post_id = 1","    comment_content = \"\"","    #act","    with pytest.raises(InvalidCommentContent) as e:","        assert create_comment(user_id,post_id,comment_content)","    ","    #assert","    assert str(e.value)   ==   \"\"","    assert     comment_content   ==   \"\"","    ","    ","@pytest.mark.django_db","def test_create_comment_with_valid_details_returns_comment_id(user,post):","    user_id = 1","    post_id = 1","    comment_content = \"post1_comment1\"","    #act","    comment_id = create_comment(user_id,post_id,comment_content)","    ","    #assert","    #extra","    comment = Comment.objects.get(id = comment_id)","    ","    assert comment.commented_by  ==  user","    assert comment.post  ==  post","    assert comment.content  ==  comment_content","    assert comment.parent_comment_id  ==  None",""],"id":18}],[{"start":{"row":107,"column":0},"end":{"row":148,"column":0},"action":"remove","lines":["@pytest.mark.django_db","def test_create_post_with_invalid_user_id_raises_InvalidUserException(user):","    #arrange","    user_id = 2","    post_content = \"post_1\"","    #act","    with pytest.raises(InvalidUserException) as e:","        assert create_post(user_id,post_content)","    ","    #assert","    #extra","    user = User.objects.filter(id = user_id)","    ","    assert str(e.value)  ==  \"\"","    assert len(user)  ==  0","    ","","@pytest.mark.django_db","def test_create_post_with_invalid_post_content_raises_InvalidPostCotent(user):","    user_id = 1","    post_content = \"\"","    #act","    with pytest.raises(InvalidPostContent) as e:","        assert create_post(user_id,post_content)","    ","    #assert","    assert str(e.value)   ==   \"\"","    assert post_content   ==   \"\"","","@pytest.mark.django_db","def test_create_post_with_valid_details_returns_post_id(user):","    user_id = 1","    post_content = \"post_1\"","    #act        ","    post_id = create_post(user_id,post_content)","    ","    #assert","    #extra","    post = Post.objects.get(id = post_id)","    ","    assert post.posted_by  ==  user",""],"id":19}]]},"ace":{"folds":[],"scrolltop":4232,"scrollleft":0,"selection":{"start":{"row":272,"column":34},"end":{"row":272,"column":34},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":247,"state":"start","mode":"ace/mode/python"}},"timestamp":1587725605721,"hash":"218e876fea302a941433b4d13ad04abee4e158a7"}