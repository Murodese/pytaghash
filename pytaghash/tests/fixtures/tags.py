# -*- coding: utf-8 -*-

import bs4

complex1 = bs4.BeautifulSoup('''
    <li>
        <div></div>
        <p></p>
        <dl>
            <dd></dd>
            <dt></dt>
        </dl>
        <p>
            <br />
        </p>
    </li>
    ''', 'lxml').li

complex1_attrib = bs4.BeautifulSoup('''
    <li>
        <div name="butt"></div>
        <p></p>
        <dl>
            <dd></dd>
            <dt></dt>
        </dl>
        <p id="poop">
            <br />
        </p>
    </li>
    ''', 'lxml').li

complex1_attrib_diff = bs4.BeautifulSoup('''
    <li name="something">
        <div id="blugh" name="butt"></div>
        <p id="stuff" name="butt"></p>
        <dl id="comments">
            <dd id="dong"></dd>
            <dt name="stuff"></dt>
        </dl>
        <p id="poop" name="butt">
            <br />
        </p>
    </li>
    ''', 'lxml').li

complex2 = bs4.BeautifulSoup('''
    <li>
        <div></div>
        <p></p>
        <dl>
            <dd></dd>
            <dt></dt>
        </dl>
        <p>
            <br />
            <br />
        </p>
    </li>
    ''', 'lxml').li

complex3 = bs4.BeautifulSoup('''
    <li>
        <div name="butt">
            <p>
                <br />
                <br />
            </p>
        </div>
        <div></div>
        <p></p>
        <a><img></img><p></p></a>
        <div></div>
        <a></a>
    </li>
    ''', 'lxml').li

complex4 = bs4.BeautifulSoup('''
    <li>
        <div></div>
        <p></p>
        <dl>
            <p></p>
        </dl>
        <dl>
            <dd></dd>
            <dt></dt>
        </dl>
        <p>
            <br />
        </p>
    </li>
    ''', 'lxml').li

nested_comments_abc = bs4.BeautifulSoup('''
<ul>
    <li>
        <a id="m_ucMessageDisplay1548290_m_anchMessageAnchor" name="m1548290"></a>
        <h3 class="">Patrick:</h3>
        <p class="date">29 Jan 2015 3:15:55pm</p>
        <p>Abbott displays all the hallmarks of a highly delusional right-man. He appears egotistical in the extreme and it should now be obvious to all that he is an extremely dangerous individual and one who should never be in a position of power, let alone being leader of a nation</p>
        <p>
            <span>
                <a class="popup" href="http://www2b.abc.net.au/tmb/View/NewMessage.aspx?b=69&amp;t=12532&amp;tn=&amp;dm=1&amp;m=1548290&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Reply</a>
            </span>
            <span>
                <a class="popup" href="http://www2b.abc.net.au/tmb/View/AlertModerator.aspx?b=69&amp;m=1548290&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">
                    Alert moderator
                </a>
            </span>
        </p>
        <ul>
            <li>
                <a id="m_ucMessageDisplay1548290_m_ucMessageChildren_m_ucMessageDisplay1548374_m_anchMessageAnchor" name="m1548374"></a>
                <h3 class="">Tony:</h3>
                <p class="date">29 Jan 2015 3:47:38pm</p>
                <p><br>
                Every footy team needs a head-kicker but you don't make him captain.<br></p>
                <p><span><a class="popup" href="http://www2b.abc.net.au/tmb/View/NewMessage.aspx?b=69&amp;t=12532&amp;tn=&amp;dm=1&amp;m=1548374&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Reply</a></span> <span><a class="popup" href="http://www2b.abc.net.au/tmb/View/AlertModerator.aspx?b=69&amp;m=1548374&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Alert moderator</a></span></p>
                <ul>
                    <li>
                        <a id="m_ucMessageDisplay1548290_m_ucMessageChildren_m_ucMessageDisplay1548374_m_ucMessageChildren_m_ucMessageDisplay1548466_m_anchMessageAnchor" name="m1548466"></a>
                        <h3 class="">JohnC:</h3>
                        <p class="date">29 Jan 2015 4:17:03pm</p>
                        <p>@Tony:<br>
                        Tony Abbott displayed all of his head kicking prowess as Leader of the Opposition so the LNP would have been fully aware of who they were appointing as team captain. The problem that they now have is that the transition from opposition to government is proving more difficult than expected and the skipper's form on the field is more about playing deep in defence than kicking goals.</p>
                        <p><span><a class="popup" href="http://www2b.abc.net.au/tmb/View/NewMessage.aspx?b=69&amp;t=12532&amp;tn=&amp;dm=1&amp;m=1548466&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Reply</a></span> <span><a class="popup" href="http://www2b.abc.net.au/tmb/View/AlertModerator.aspx?b=69&amp;m=1548466&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Alert moderator</a></span></p>
                    </li>
                    <li>
                        <a id="m_ucMessageDisplay1548290_m_ucMessageChildren_m_ucMessageDisplay1548374_m_ucMessageChildren_m_ucMessageDisplay1548785_m_anchMessageAnchor" name="m1548785"></a>
                        <h3 class="">Arthur:</h3>
                        <p class="date">29 Jan 2015 6:07:58pm</p>
                        <p>Like<br></p>\
                        <p><span><a class="popup" href="http://www2b.abc.net.au/tmb/View/NewMessage.aspx?b=69&amp;t=12532&amp;tn=&amp;dm=1&amp;m=1548785&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Reply</a></span> <span><a class="popup" href="http://www2b.abc.net.au/tmb/View/AlertModerator.aspx?b=69&amp;m=1548785&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Alert moderator</a></span></p>
                    </li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <a id="m_ucMessageDisplay1548290_m_ucMessageChildren_m_ucMessageDisplay1548374_m_ucMessageChildren_m_ucMessageDisplay1548466_m_anchMessageAnchor" name="m1548466"></a>
        <h3 class="">JohnC:</h3>
        <p class="date">29 Jan 2015 4:17:03pm</p>
        <p>@Tony:<br>
        Tony Abbott displayed all of his head kicking prowess as Leader of the Opposition so the LNP would have been fully aware of who they were appointing as team captain. The problem that they now have is that the transition from opposition to government is proving more difficult than expected and the skipper's form on the field is more about playing deep in defence than kicking goals.</p>
        <p><span><a class="popup" href="http://www2b.abc.net.au/tmb/View/NewMessage.aspx?b=69&amp;t=12532&amp;tn=&amp;dm=1&amp;m=1548466&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Reply</a></span> <span><a class="popup" href="http://www2b.abc.net.au/tmb/View/AlertModerator.aspx?b=69&amp;m=1548466&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Alert moderator</a></span></p>
    </li>
    <li>
        <a id="m_ucMessageDisplay1548290_m_ucMessageChildren_m_ucMessageDisplay1548374_m_ucMessageChildren_m_ucMessageDisplay1548785_m_anchMessageAnchor" name="m1548785"></a>
        <h3 class="">Arthur:</h3>
        <p class="date">29 Jan 2015 6:07:58pm</p>
        <p>Like<br></p>\
        <p><span><a class="popup" href="http://www2b.abc.net.au/tmb/View/NewMessage.aspx?b=69&amp;t=12532&amp;tn=&amp;dm=1&amp;m=1548785&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Reply</a></span> <span><a class="popup" href="http://www2b.abc.net.au/tmb/View/AlertModerator.aspx?b=69&amp;m=1548785&amp;tpa=&amp;r=%2ftmb%2fView%2fMessage.aspx%3fb%3d69%26t%3d12532%26a%3d0%26ps%3d50%26tpa%3d%26uto%3d1%26dm%3d4%26ci%3d0%26pd%3d1%26so%3dDateTime%26soa%3dTrue%26p%3d1%26p2%3d0">Alert moderator</a></span></p>
    </li>
</ul>
''', 'lxml')

nested_comments_kotaku = bs4.BeautifulSoup('''
<div class="post-meta" id="comments">
    <div class="ribbon-separator dark">
        <span class="colour sprite sprite-comments" style="font-style: italic"></span>

        <h4 class="pull-left">Discuss</h4><span class="sub pull-right">23 Comments | <a class="anchor-link track_action" data-tracking-name="Jump to Reply Box" href="#respond">Reply <i class="icon-chevron-down icon-white"></i></a></span>
    </div>

    <ul class="commentlist">
        <li class="comment depth-1" data-comment-id="3260248" id="comment-3260248">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://1.gravatar.com/avatar/ffae2ad1f2fda5478ac40f003539f6ad?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260248" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260248" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260248" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="dre666">
                            dre666 <small><a href="/user/dre666/">@dre666</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:17 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Rally x comes to mind. Colours are wrong though..</p><input class="original_comment hide" type="hidden" value="Rally x comes to mind. Colours are wrong though..">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260248#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260248"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260248" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>
        </li>

        <li class="comment depth-1" data-comment-id="3260252" id="comment-3260252">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://0.gravatar.com/avatar/056291335d7a67feb26739dead5d52c5?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260252" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260252" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260252" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="mickd">
                            mickd <small><a href="/user/mickd/">@mickd</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:18 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>what the hell is this "Also on Kotaku"</p>

                        <p>new?</p>

                        <p>can this please go after comments section</p><input class="original_comment hide" type="hidden" value="what the hell is this &quot;Also on Kotaku&quot; new? can this please go after comments section">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260252#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260252"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-success" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260252" data-toggle="modal" title="View Voters">8</a></span></span>
                    </div>
                </div>
            </div><br>

            <ul class="children">
                <li class="comment depth-2" data-comment-id="3260360" id="comment-3260360">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://0.gravatar.com/avatar/0993ff5db94278ace29aec8c830da215?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260360" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260360" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260360" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="edenist">
                                    edenist <small><a href="/user/edenist/">@edenist</a></small>
                                </div>

                                <div class="meta">
                                    March 10, 2015 12:59 pm
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>There already is one at the bottom after comments, for the whole Allure network. Seems they've put one up top too.</p>

                                <p>I agree I really find it visibly irritating when there is advertising content between the article and the comments. Just forcing more content in the readers face any way possible.</p>

                                <p>EDIT: It's clear they do it for people who come to an article via direct link [from reddit, facebook etc], to expose them to content on the site elsewhere. But for those who browse the front page, we've already seen the articles it displays, I don't want to see them again. Perhaps have a check to disable the middle ad's if you come from the main page?</p>

                                <p class="meta">Last edited March 10, 2015 1:01 pm</p><input class="original_comment hide" type="hidden" value="There already is one at the bottom after comments, for the whole Allure network. Seems they've put one up top too. I agree I really find it visibly irritating when there is advertising content between the article and the comments. Just forcing more content in the readers face any way possible. EDIT: It's clear they do it for people who come to an article via direct link [from reddit, facebook etc], to expose them to content on the site elsewhere. But for those who browse the front page, we've already seen the articles it displays, I don't want to see them again. Perhaps have a check to disable the middle ad's if you come from the main page?">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260360#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260360"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260360" data-toggle="modal" title="View Voters">0</a></span></span>
                            </div>
                        </div>
                    </div><br>
                </li>
            </ul>
        </li>

        <li class="comment depth-1" data-comment-id="3260253" id="comment-3260253">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://0.gravatar.com/avatar/62aeeba5ef45e82d2f6b9a7c4e8f294f?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260253" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260253" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260253" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="Talicca">
                            Talicca <small><a href="/user/talicca/">@talicca</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:19 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Is that... Adventure? (Atari).</p><input class="original_comment hide" type="hidden" value="Is that... Adventure? (Atari).">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260253#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260253"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260253" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>

            <ul class="children">
                <li class="comment depth-2" data-comment-id="3260283" id="comment-3260283">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://1.gravatar.com/avatar/f58277fc869eb4bbbfe36effc8ed9352?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260283" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260283" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260283" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="WiseHacker">
                                    WiseHacker <small><a href="/user/wisehacker/">@wisehacker</a></small>
                                </div>

                                <div class="meta">
                                    March 10, 2015 12:28 pm
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>Dayum. Beat me to it.</p><input class="original_comment hide" type="hidden" value="Dayum. Beat me to it.">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260283#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260283"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260283" data-toggle="modal" title="View Voters">0</a></span></span>
                            </div>
                        </div>
                    </div><br>
                </li>

                <li class="comment depth-2" data-comment-id="3260285" id="comment-3260285">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://0.gravatar.com/avatar/2671376cdc60fb70b45a7f2832342789?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260285" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260285" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260285" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="gnawnborg">
                                    gnawnborg <small><a href="/user/gnawnborg/">@gnawnborg</a></small>
                                </div>

                                <div class="meta">
                                    March 10, 2015 12:29 pm
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>Was thinking that as well, but don't think it's quite right</p><input class="original_comment hide" type="hidden" value="Was thinking that as well, but don't think it's quite right">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260285#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260285"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260285" data-toggle="modal" title="View Voters">0</a></span></span>
                            </div>
                        </div>
                    </div><br>
                </li>
            </ul>
        </li>

        <li class="comment depth-1" data-comment-id="3260254" id="comment-3260254">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://0.gravatar.com/avatar/c21039d2f9fa4de64662e7af672a7656?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260254" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260254" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260254" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="Beavwa">
                            Beavwa <small><a href="/user/beavwa/">@beavwa</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:19 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Reminds me of Combat on Atari but there's too much wall and not enough open space.</p><input class="original_comment hide" type="hidden" value="Reminds me of Combat on Atari but there's too much wall and not enough open space.">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260254#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260254"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260254" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>

            <ul class="children">
                <li class="comment depth-2" data-comment-id="3260255" id="comment-3260255">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://0.gravatar.com/avatar/c21039d2f9fa4de64662e7af672a7656?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260255" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260255" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260255" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="Beavwa">
                                    Beavwa <small><a href="/user/beavwa/">@beavwa</a></small>
                                </div>

                                <div class="meta">
                                    March 10, 2015 12:20 pm
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>Found the answer but not posting it since I don't Remember This...</p><input class="original_comment hide" type="hidden" value="Found the answer but not posting it since I don't Remember This...">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260255#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260255"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260255" data-toggle="modal" title="View Voters">0</a></span></span>
                            </div>
                        </div>
                    </div><br>
                </li>
            </ul>
        </li>

        <li class="comment depth-1" data-comment-id="3260257" id="comment-3260257">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://1.gravatar.com/avatar/5a217a1aab6c8813cdb7a3743fbd7c11?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260257" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260257" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260257" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="lemonmule">
                            lemonmule <small><a href="/user/lemonmule/">@lemonmule</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:21 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>I feel like this might be an atari game..</p>

                        <p>This "also on kotaku" section isn't so bad on browser, but my God ! On mobile it's so in your face and obstructing. Please change it for mobile viewing please.</p><input class="original_comment hide" type="hidden" value="I feel like this might be an atari game.. This &quot;also on kotaku&quot; section isn't so bad on browser, but my God ! On mobile it's so in your face and obstructing. Please change it for mobile viewing please.">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260257#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260257"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260257" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>
        </li>

        <li class="comment depth-1" data-comment-id="3260262" id="comment-3260262">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://1.gravatar.com/avatar/d71c37e81746d0a6a9eda145bd09d5ac?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260262" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260262" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260262" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="Live Long And Prosper">
                            Live Long And Prosper <small><a href="/user/cufcfan616/">@cufcfan616</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:23 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>If it was a black background I'd say Bubble Bobble but it's not :(</p><input class="original_comment hide" type="hidden" value="If it was a black background I'd say Bubble Bobble but it's not :(">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260262#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260262"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260262" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>

            <ul class="children">
                <li class="comment depth-2" data-comment-id="3261606" id="comment-3261606">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://1.gravatar.com/avatar/16e105590c20bb3de5f39ed031a4a304?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3261606" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3261606" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3261606" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="matthew">
                                    matthew <small><a href="/user/matthew/">@matthew</a></small>
                                </div>

                                <div class="meta">
                                    March 11, 2015 9:30 am
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>I played Bubble Bobble for a few hours on the weekend. So many happy memories :)</p><input class="original_comment hide" type="hidden" value="I played Bubble Bobble for a few hours on the weekend. So many happy memories :)">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3261606#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3261606"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3261606" data-toggle="modal" title="View Voters">0</a></span></span>
                            </div>
                        </div>
                    </div><br>
                </li>
            </ul>
        </li>

        <li class="comment depth-1" data-comment-id="3260266" id="comment-3260266">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://0.gravatar.com/avatar/a8780bff92bcc1d8302b5fca88dcead8?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260266" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260266" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260266" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="poita">
                            poita <small><a href="/user/poita/">@poita</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:24 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Adventure on the 2600?</p><input class="original_comment hide" type="hidden" value="Adventure on the 2600?">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260266#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260266"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260266" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>
        </li>

        <li class="comment depth-1" data-comment-id="3260273" id="comment-3260273">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://0.gravatar.com/avatar/a8780bff92bcc1d8302b5fca88dcead8?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260273" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260273" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260273" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="poita">
                            poita <small><a href="/user/poita/">@poita</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:26 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Or maybe slot racers on the 2600. My brother and I used to pound that game.</p><input class="original_comment hide" type="hidden" value="Or maybe slot racers on the 2600. My brother and I used to pound that game.">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260273#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260273"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260273" data-toggle="modal" title="View Voters">3</a></span></span>
                    </div>
                </div>
            </div><br>

            <ul class="children">
                <li class="comment depth-2" data-comment-id="3260347" id="comment-3260347">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://0.gravatar.com/avatar/82f234eb541549955d3775b43aebefbd?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260347" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260347" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260347" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="konaju">
                                    konaju <small><a href="/user/konaju/">@konaju</a></small>
                                </div>

                                <div class="meta">
                                    March 10, 2015 12:52 pm
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>It is indeed.<br>
                                <a href="http://www.atarimania.com/game-atari-2600-vcs-slot-racers_7374.html" rel="nofollow">http://www.atarimania.com/game-atari-2600-vcs-slot-racers_7374.html</a></p><input class="original_comment hide" type="hidden" value="It is indeed. http://www.atarimania.com/game-atari-2600-vcs-slot-racers_7374.html">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260347#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260347"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260347" data-toggle="modal" title="View Voters">0</a></span></span>
                            </div>
                        </div>
                    </div><br>
                </li>

                <li class="comment depth-2" data-comment-id="3260471" id="comment-3260471">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://1.gravatar.com/avatar/713ae57e2ca20d0e10e82746322ef459?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260471" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260471" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260471" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="WhitePointer">
                                    WhitePointer <small><a href="/user/whitepointer/">@whitepointer</a></small>
                                </div>

                                <div class="meta">
                                    March 10, 2015 1:47 pm
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>Yup, looks like it. Bravo.</p>

                                <p><a href="https://www.youtube.com/watch?v=yyO_G8OBu9w" rel="nofollow">https://www.youtube.com/watch?v=yyO_G8OBu9w</a></p>

                                <p>I remember playing this game, and it was pretty bad :/</p>

                                <p class="meta">Last edited March 10, 2015 1:49 pm</p><input class="original_comment hide" type="hidden" value="Yup, looks like it. Bravo. https://www.youtube.com/watch?v=yyO_G8OBu9w I remember playing this game, and it was pretty bad :/">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260471#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260471"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260471" data-toggle="modal" title="View Voters">0</a></span></span>
                            </div>
                        </div>
                    </div><br>

                    <ul class="children">
                        <li class="comment depth-3" data-comment-id="3260633" id="comment-3260633">
                            <div class="comment_container">
                                <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://0.gravatar.com/avatar/a8780bff92bcc1d8302b5fca88dcead8?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                                <ul class="comment_config">
                                    <li class="showhide">
                                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                                    </li>

                                    <li class="permalink">
                                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260633" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260633" style="font-style: italic" title="Permalink"></a>
                                    </li>

                                    <li class="report">
                                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260633" style="font-style: italic" title="Login to report this comment"></a>
                                    </li>
                                </ul>

                                <div class="comment-content-wrap">
                                    <div class="comment-heading">
                                        <div class="title" data-display-name="poita">
                                            poita <small><a href="/user/poita/">@poita</a></small>
                                        </div>

                                        <div class="meta">
                                            March 10, 2015 3:03 pm
                                        </div>
                                    </div>

                                    <div class="comment-content">
                                        <p>We only had three games at the time, so we thought it was awesome.</p><input class="original_comment hide" type="hidden" value="We only had three games at the time, so we thought it was awesome.">
                                    </div>

                                    <div class="comment_reply tracking_article_comments">
                                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260633#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260633"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260633" data-toggle="modal" title="View Voters">0</a></span></span>
                                    </div>
                                </div>
                            </div><br>
                        </li>
                    </ul>
                </li>

                <li class="comment depth-2" data-comment-id="3260611" id="comment-3260611">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://1.gravatar.com/avatar/379afc0c121f0b9ab36b11fa2bc59988?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260611" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260611" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260611" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="oggob">
                                    oggob <small><a href="/user/oggob/">@oggob</a></small>
                                </div>

                                <div class="meta">
                                    March 10, 2015 2:56 pm
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>Never seen this one before, but it's basically a bad Combat... lol</p><input class="original_comment hide" type="hidden" value="Never seen this one before, but it's basically a bad Combat... lol">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260611#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260611"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260611" data-toggle="modal" title="View Voters">0</a></span></span>
                            </div>
                        </div>
                    </div><br>
                </li>
            </ul>
        </li>

        <li class="comment depth-1" data-comment-id="3260300" id="comment-3260300">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://1.gravatar.com/avatar/bdd66505554b75489fc56a20b12b2e43?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260300" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260300" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260300" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="bob3">
                            bob3 <small>Guest</small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:32 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Mark obviously went to the classic games postmortem at GDC on Adventure.</p><input class="original_comment hide" type="hidden" value="Mark obviously went to the classic games postmortem at GDC on Adventure.">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260300#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260300"><a class="btn btn-mini disabled icon-chevron-up" style="font-style: italic" title="You can't vote on your own comment"></a> <a class="btn btn-mini disabled icon-chevron-down" style="font-style: italic" title="You can't vote on your own comment"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260300" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>
        </li>

        <li class="comment depth-1" data-comment-id="3260311" id="comment-3260311">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://0.gravatar.com/avatar/0d9de22c790dc6b1e880868a88c331e5?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260311" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260311" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260311" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="Zetrox2k">
                            Zetrox2k <small><a href="/user/zetrox2k/">@zetrox2k</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:36 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Pacman - Atari 2600?</p><input class="original_comment hide" type="hidden" value="Pacman - Atari 2600?">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260311#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260311"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260311" data-toggle="modal" title="View Voters">1</a></span></span>
                    </div>
                </div>
            </div><br>

            <ul class="children">
                <li class="comment depth-2" data-comment-id="3260543" id="comment-3260543">
                    <div class="comment_container">
                        <div class="comment_avatar"><img alt="" class="avatar avatar-24 photo" height="24" src="http://1.gravatar.com/avatar/f5ba540c1d18568a6dd513d7a59cece0?s=24&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D24&amp;r=G" width="24"></div>

                        <ul class="comment_config">
                            <li class="showhide">
                                <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                            </li>

                            <li class="permalink">
                                <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260543" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260543" style="font-style: italic" title="Permalink"></a>
                            </li>

                            <li class="report">
                                <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260543" style="font-style: italic" title="Login to report this comment"></a>
                            </li>
                        </ul>

                        <div class="comment-content-wrap">
                            <div class="comment-heading">
                                <div class="title" data-display-name="pupp3tmast3r">
                                    pupp3tmast3r <small><a href="/user/pupp3tmast3r/">@pupp3tmast3r</a></small>
                                </div>

                                <div class="meta">
                                    March 10, 2015 2:21 pm
                                </div>
                            </div>

                            <div class="comment-content">
                                <p>This. The centre arrangement of squares looks a lot like Pacman.</p><input class="original_comment hide" type="hidden" value="This. The centre arrangement of squares looks a lot like Pacman.">
                            </div>

                            <div class="comment_reply tracking_article_comments">
                                <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260543#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260543"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260543" data-toggle="modal" title="View Voters">1</a></span></span>
                            </div>
                        </div>
                    </div><br>
                </li>
            </ul>
        </li>

        <li class="comment depth-1" data-comment-id="3260316" id="comment-3260316">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://0.gravatar.com/avatar/ac4ed35c82c0f172c46b846fbb56891f?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260316" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260316" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260316" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="over30yearsofsharing">
                            over30yearsofsharing <small><a href="/user/over30yearsofsharing/">@over30yearsofsharing</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 12:37 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>its minuture golf on the atari 2600</p><input class="original_comment hide" type="hidden" value="its minuture golf on the atari 2600">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260316#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260316"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260316" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>
        </li>

        <li class="comment depth-1" data-comment-id="3260476" id="comment-3260476">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://0.gravatar.com/avatar/25ca23a2abec96ecd1b85954bca4dfa2?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260476" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260476" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260476" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="decoy">
                            decoy <small><a href="/user/decoy/">@decoy</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 1:50 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Biker Mice from MArs</p><input class="original_comment hide" type="hidden" value="Biker Mice from MArs">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260476#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260476"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260476" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>
        </li>

        <li class="comment depth-1" data-comment-id="3260801" id="comment-3260801">
            <div class="comment_container">
                <div class="comment_avatar"><img alt="" class="avatar avatar-32 photo" height="32" src="http://1.gravatar.com/avatar/3dd231727df49b9a6799f581191034d3?s=32&amp;d=http%3A%2F%2Fedge.alluremedia.com.au%2Fassets%2Ftechnetwork%2Fimg%2Fkotaku%2Fgravatar.jpg%3Fs%3D32&amp;r=G" width="32"></div>

                <ul class="comment_config">
                    <li class="showhide">
                        <a class="track_action icon-minus" data-tracking-name="Toggle Comment Collapse" style="font-style: italic" title="Hide"></a>
                    </li>

                    <li class="permalink">
                        <a class="track_action icon-bookmark" data-target="/wp-admin/admin-ajax.php?id=get_permalink&amp;link=http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260801" data-toggle="modal" data-tracking-name="Permalink" href="http://www.kotaku.com.au/2015/03/remember-this-735/comment-page-1/#comment-3260801" style="font-style: italic" title="Permalink"></a>
                    </li>

                    <li class="report">
                        <a class="disabled track_action icon-flag" data-target="/wp-admin/admin-ajax.php?id=login_to_report" data-toggle="modal" data-tracking-name="Login to Report" id="report-3260801" style="font-style: italic" title="Login to report this comment"></a>
                    </li>
                </ul>

                <div class="comment-content-wrap">
                    <div class="comment-heading">
                        <div class="title" data-display-name="grim-one">
                            grim-one <small><a href="/user/grim-one/">@grim-one</a></small>
                        </div>

                        <div class="meta">
                            March 10, 2015 4:31 pm
                        </div>
                    </div>

                    <div class="comment-content">
                        <p>Reminds me of Wizard of Wor, but it isn't quite right for my C64 copy</p><input class="original_comment hide" type="hidden" value="Reminds me of Wizard of Wor, but it isn't quite right for my C64 copy">
                    </div>

                    <div class="comment_reply tracking_article_comments">
                        <a class="comment-reply-link" data-tracking-name="Reply" href="/2015/03/remember-this-735/?replytocom=3260801#respond" title="Reply"><i class="icon-share"></i> Reply</a> <span class="comment-vote" data-comment-id="3260801"><a class="btn btn-mini disabled icon-chevron-up" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Up Vote"></a> <a class="btn btn-mini disabled icon-chevron-down" data-target="/wp-admin/admin-ajax.php?id=login_to_vote" data-toggle="modal" style="font-style: italic" title="Down Vote"></a> <span class="vote-count"><a class="btn btn-mini btn-normal" data-target="/wp-admin/admin-ajax.php?id=view_votes&amp;comment=3260801" data-toggle="modal" title="View Voters">0</a></span></span>
                    </div>
                </div>
            </div><br>
        </li>
    </ul>

    <div class="well" id="respond">
        <a class="btn btn-mini pull-right track_action" data-tracking-name="Cancel Reply" href="http://www.kotaku.com.au/2015/03/remember-this-735/#respond" id="cancel-comment-reply-link" rel="nofollow" style="display:none;">Cancel Reply</a>

        <h3 id="reply-title">Join the discussion!</h3><a class="btn btn-mini pull-right track_action" data-tracking-name="Back to log In" href="/user/login/" id="close_comment_login_panel">Back to log In</a>

        <div class="clearfix" id="comment_login_panel">
            <div class="panel">
                <a class="btn btn-block btn-primary track_action" data-target="/wp-admin/admin-ajax.php?id=log_in" data-toggle="modal" data-tracking-name="Log In" href="/user/login/"><i class="icon-user icon-white"></i> Log In</a>
            </div>

            <div class="panel">
                <a class="btn btn-block track_action" data-target="/wp-admin/admin-ajax.php?id=user_registration" data-toggle="modal" data-tracking-name="Register" href="/user/register/"><i class="icon-plus"></i> Register</a>
            </div>

            <div class="panel last">
                <a class="btn btn-block track_action" data-tracking-name="Guest Access" id="show_comment_guest_panel"><i class="icon-chevron-down"></i> Guest Access</a>
            </div>
        </div>

        <form action="http://www.kotaku.com.au/2015/03/remember-this-735/" id="comment_form" method="post" name="comment_form" novalidate="novalidate" style="display: none;">
            <div class="comment_text_container clearfix" id="comment_guest_panel">
                <div class="pull-left">
                    <label class="placeholder" for="guest_name">Your Name</label> <input class="input-xlarge" id="guest_name" name="guest_name" placeholder="Your Name" type="text" value="">
                </div>

                <div class="pull-right">
                    <label class="placeholder" for="guest_email">Your Email</label> <input class="input-xlarge" id="guest_email" name="guest_email" placeholder="Your Email" type="text" value="">
                </div>
            </div>

            <div class="comment_textarea_container html_editor">
                <label class="placeholder" for="comment_content">Join the discussion!</label>

                <div class="btn-toolbar html_editor_bar" data-target="#comment_content">
                    <div class="btn-group">
                        <a class="btn bold icon-bold" style="font-style: italic" title="Bold"></a> <a class="btn italic icon-italic" style="font-style: italic" title="Italic"></a> <a class="btn underline icon-underline" style="font-style: italic" title="Underline"></a> <a class="btn quote icon-comment-alt" style="font-style: italic" title="Quote"></a> <a class="btn mention icon-bullhorn" style="font-style: italic" title="@ Mention User"></a> <a class="btn spoiler icon-eye-open" style="font-style: italic" title="Toggle Spoiler Content"></a>
                    </div>
                </div>
                <textarea class="comment_textarea input-xlarge" id="comment_content" name="comment_content" placeholder="Join the discussion!" style="overflow: hidden; height: 80px;">
</textarea>
            </div>

            <div class="pull-left" id="reply-status">
                <div class="alert alert-success no-close">
                    You are starting a new discussion
                </div>
            </div>

            <div class="form-submit pull-right">
                <input class="btn btn-primary track_action" data-tracking-name="Submit New Comment" id="comment_submit" name="submit_comment" type="submit" value="Submit"> <input id="comment_post_ID" name="comment_post_ID" type="hidden" value="697351"> <input id="comment_parent" name="comment_parent" type="hidden" value="0"> <input id="post_comment_wpnonce" name="post_comment_wpnonce" type="hidden" value="88aa68ea66"><input name="_wp_http_referer" type="hidden" value="/2015/03/remember-this-735/"> <input id="author" name="author" style="display:none;" tabindex="101" type="text" value=""> <input id="email" name="email" style="display:none;" tabindex="102" type="text" value=""> <input id="url" name="url" style="display:none;" tabindex="103" type="text" value="">
                <textarea name="comment" style="display:none;" tabindex="104">
</textarea> <input name="datetime" type="hidden" value="1426039439"> <input name="js_data" type="hidden" value="">
            </div>
        </form>
    </div>
</div>
''', 'lxml')

nested_comments_disqus = bs4.BeautifulSoup('''
<div id="posts">
    <div id="form">
        <form class="reply">
            <div class="postbox">
                <div></div>

                <div class="avatar">
                    <span class="user"><img alt="Avatar" data-role="user-avatar" src="//a.disquscdn.com/next/embed/assets/img/noavatar92.b677f9ddbee6f4bb22f473ae3bd61b85.png"></span>
                </div>

                <div class="textarea-wrapper" data-role="textarea" dir="auto">
                    <div>
                        <span class="placeholder">Join the discussion…</span>

                        <div class="textarea" contenteditable="true" data-role="editable" style="overflow: auto; max-height: 350px;" tabindex="0">
                            <p><br></p>
                        </div>

                        <div style="display: none;">
                            <ul class="suggestions">
                                <li class="header">
                                    <h5>in this conversation</h5>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="media-drag-hover" data-role="drag-drop-placeholder" style="display: none">
                        <div class="drag-text">
                            ⬇ Drag and drop your images here to upload them.
                        </div>
                    </div>

                    <div class="media-preview empty" data-role="media-preview">
                        <ul data-role="media-legacy-list"></ul>

                        <ul data-role="media-progress-list"></ul>

                        <ul data-role="media-rich-list"></ul>

                        <div class="media-expanded empty" data-role="media-preview-expanded"><img alt="Media preview placeholder" data-role="media-preview-expanded-image" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="></div>
                    </div>

                    <div class="edit-alert"></div>

                    <div class="post-actions">
                        <ul class="wysiwyg">
                            <li>
                                <a class="attach" data-action="attach" href="#" tabindex="-1" title="Upload Images"><span>Attach</span></a> <input accept="image/*" class="regular" data-role="media-upload" tabindex="-1" type="file">
                            </li>
                        </ul>
                    </div>
                </div>

                <div data-role="login-form">
                    <div>
                        <section class="auth-section logged-out">
                            <div class="connect">
                                <h6>Sign in with</h6>

                                <ul class="services login-buttons" data-role="login-menu">
                                    <li class="auth-disqus"><button class="icon-disqus" data-action="auth:disqus" style="font-style: italic" title="Disqus" type="button"></button></li>

                                    <li class="auth-facebook"><button class="icon-facebook-circle" data-action="auth:facebook" style="font-style: italic" title="Facebook" type="button"></button></li>

                                    <li class="auth-twitter"><button class="icon-twitter-circle" data-action="auth:twitter" style="font-style: italic" title="Twitter" type="button"></button></li>

                                    <li class="auth-google"><button class="icon-google-plus-circle" data-action="auth:google" style="font-style: italic" title="Google" type="button"></button></li>
                                </ul>
                            </div>

                            <div class="guest">
                                <h6 class="guest-form-title">or register with Disqus</h6>

                                <div class="what-is-disqus help-icon">
                                    <div class="tooltip show" id="rules">
                                        <h3>Disqus is a conversation network</h3>

                                        <ul>
                                            <li><span>Disqus never moderates or censors. The rules on this community are its own.</span></li>

                                            <li><span>Your email is safe with us. It's only used for moderation and optional notifications.</span></li>

                                            <li><span>Don't be a jerk or do anything illegal. Everything is easier that way.</span></li>
                                        </ul>

                                        <p class="clearfix"><a class="btn btn-small" href="https://docs.disqus.com/kb/terms-and-policies/" target="_blank">Read full terms and conditions</a></p>
                                    </div>
                                </div>

                                <p class="input-wrapper"><input dir="auto" id="view288_display_name" maxlength="30" name="display_name" placeholder="Name" type="text"></p>

                                <div class="guest-details" data-role="guest-details">
                                    <p class="input-wrapper"><input dir="auto" id="view288_email" name="email" placeholder="Email" type="email"></p>

                                    <p class="input-wrapper"><input dir="auto" id="view288_password" name="password" placeholder="Password" type="password"></p><input name="author-guest" style="display:none" type="checkbox">
                                </div>
                            </div>

                            <div class="proceed">
                                <button class="btn submit" type="submit"><span class="icon-proceed"></span></button>
                            </div>
                        </section>
                    </div>
                </div>
            </div>
        </form>
    </div><button class="alert realtime" data-role="realtime-notification" style="display: none;"></button>

    <div id="no-posts" style="display: none;">
        Be the first to comment.
    </div>

    <ul class="post-list" id="post-list">
        <li class="post" id="post-1896292556">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="megaseven" href="https://disqus.com/by/megaseven/"><img alt="Avatar" data-role="user-avatar" data-user="66214858" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="megaseven" href="https://disqus.com/by/megaseven/">DJ Schway</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896292556" title="Monday, March 9, 2015 6:22 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>Welp, I'm depressed. Not only was he a protector of the people, but he was there to buy a gift for his son. /sigh</p>

                                    <p>Also, way to go Ramone. Go back to the scene of the crime like a dingus and get caught.</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-28" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">28</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896292556">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896292556">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children">
                <li class="post" id="post-1896348335">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="extatix" href="https://disqus.com/by/extatix/"><img alt="Avatar" data-role="user-avatar" data-user="63760512" src="//a.disquscdn.com/uploads/users/6376/512/avatar92.jpg?1426002765"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="extatix" href="https://disqus.com/by/extatix/">Giovanni</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896292556"><i class="icon-forward" title="in reply to"></i> DJ Schway</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896348335" title="Monday, March 9, 2015 7:33 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>Other "news outlets" differ on the Williams part.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896348335">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896348335">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children"></ul>
                </li>
            </ul>
        </li>

        <li class="post" id="post-1896292863">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="modernmethod-177e32c9135cbd89ce90cb7cebf0270c" href="https://disqus.com/by/modernmethod-177e32c9135cbd89ce90cb7cebf0270c/"><img alt="Avatar" data-role="user-avatar" data-user="31408399" src="//a.disquscdn.com/uploads/users/3140/8399/avatar92.jpg?1425957114"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-177e32c9135cbd89ce90cb7cebf0270c" href="https://disqus.com/by/modernmethod-177e32c9135cbd89ce90cb7cebf0270c/">ph00p</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896292863" title="Monday, March 9, 2015 6:23 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>Too soon for the "blame Battlefield:Hardline" comment?</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-2" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896292863">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896292863">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children">
                <li class="post" id="post-1896312124">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="modernmethod-73043400d135f80e05f12572b60b2b17" href="https://disqus.com/by/modernmethod-73043400d135f80e05f12572b60b2b17/"><img alt="Avatar" data-role="user-avatar" data-user="102066339" src="//a.disquscdn.com/uploads/users/10206/6339/avatar92.jpg?1426037586"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-73043400d135f80e05f12572b60b2b17" href="https://disqus.com/by/modernmethod-73043400d135f80e05f12572b60b2b17/">JBroXNari99</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896292863"><i class="icon-forward" title="in reply to"></i> ph00p</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896312124" title="Monday, March 9, 2015 6:49 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>Yeah, too soon.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-8" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">8</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896312124">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896312124">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children">
                        <li class="post" id="post-1896593133">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="cyrylthewolf" href="https://disqus.com/by/cyrylthewolf/"><img alt="Avatar" data-role="user-avatar" data-user="1621535" src="//a.disquscdn.com/uploads/users/162/1535/avatar92.jpg?1425911676"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="cyrylthewolf" href="https://disqus.com/by/cyrylthewolf/">cyrylthewolf</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896312124"><i class="icon-forward" title="in reply to"></i> JBroXNari99</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896593133" title="Monday, March 9, 2015 9:40 PM">2 days ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>FOREVER.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-3" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">3</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896593133">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1896593133">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children"></ul>
                        </li>

                        <li class="post" id="post-1897887213">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="modernmethod-76a969fc1d1adaac804d2dabce3451f5" href="https://disqus.com/by/modernmethod-76a969fc1d1adaac804d2dabce3451f5/"><img alt="Avatar" data-role="user-avatar" data-user="34208920" src="//a.disquscdn.com/uploads/users/3420/8920/avatar92.jpg?1426042481"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-76a969fc1d1adaac804d2dabce3451f5" href="https://disqus.com/by/modernmethod-76a969fc1d1adaac804d2dabce3451f5/">Kanten</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896312124"><i class="icon-forward" title="in reply to"></i> JBroXNari99</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1897887213" title="Tuesday, March 10, 2015 7:13 AM">a day ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>It's never too soon to throw mud at EA.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1897887213">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1897887213">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children"></ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>

        <li class="post" id="post-1896302935">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="renaudb90" href="https://disqus.com/by/renaudb90/"><img alt="Avatar" data-role="user-avatar" data-user="79133339" src="//a.disquscdn.com/uploads/users/7913/3339/avatar92.jpg?1382807761"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="renaudb90" href="https://disqus.com/by/renaudb90/">RenaudB90</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896302935" title="Monday, March 9, 2015 6:37 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>Well that's just the worst thing ever.</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-24" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">24</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896302935">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896302935">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children"></ul>
        </li>

        <li class="post" id="post-1896305588">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="modernmethod-0a63135f0a24d85527a1b30f0aeccaa5" href="https://disqus.com/by/modernmethod-0a63135f0a24d85527a1b30f0aeccaa5/"><img alt="Avatar" data-role="user-avatar" data-user="34201003" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-0a63135f0a24d85527a1b30f0aeccaa5" href="https://disqus.com/by/modernmethod-0a63135f0a24d85527a1b30f0aeccaa5/">Devin Lee</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896305588" title="Monday, March 9, 2015 6:41 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>most cop news now days is about how the asshole cops get away with shooting people point blank for pretty much no reason, and its a good cop that gets shot in a robbery...</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-4" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">4</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896305588">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896305588">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children">
                <li class="post" id="post-1896312595">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/"><img alt="Avatar" data-role="user-avatar" data-user="104252315" src="//a.disquscdn.com/uploads/users/10425/2315/avatar92.jpg?1425200107"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/">Nekrosys</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896305588"><i class="icon-forward" title="in reply to"></i> Devin Lee</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896312595" title="Monday, March 9, 2015 6:49 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>See, I'm under the impression that a lot (most - almost all) cops are of good intent. I may be a little biased considering I have an aunt who works for the police, however.</p>

                                            <p>Putting aside the political and social debates about police, however, the act of intentionally taking another person's life (aside from legitimate cases of self-defence and the like) is beyond reprehensible.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-15" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">15</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896312595">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896312595">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children">
                        <li class="post" id="post-1898058633">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/"><img alt="Avatar" data-role="user-avatar" data-user="51506332" src="//a.disquscdn.com/uploads/users/5150/6332/avatar92.jpg?1369207961"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/">Tiredman</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896312595"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898058633" title="Tuesday, March 10, 2015 9:14 AM">a day ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>yeah, i am a bit different. I have no issues with cops myself, but so many of my family members who live in smaller areas have mostly horror stories about cops. Getting beat up for no reason, and being unable to do anything about it because in small towns a lot of the folks in charge are usually related in some way or part of some of the same groups so they tend to stick together.</p>

                                                    <p>There are plenty of good cops, but I wouldn't go with "almost all". I would say probably 60/40 to 70/30 on the good / not so good ratio.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898058633">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1898058633">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children">
                                <li class="post" id="post-1898092831">
                                    <div></div>

                                    <div class="post-content" data-role="post-content">
                                        <ul class="post-menu dropdown" data-role="menu">
                                            <li class="collapse">
                                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                            </li>

                                            <li class="expand">
                                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                            </li>

                                            <li class="">
                                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                            </li>
                                        </ul>

                                        <div class="indicator"></div>

                                        <div class="avatar hovercard">
                                            <a class="user" data-action="profile" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/"><img alt="Avatar" data-role="user-avatar" data-user="104252315" src="//a.disquscdn.com/uploads/users/10425/2315/avatar92.jpg?1425200107"></a>
                                        </div>

                                        <div class="post-body">
                                            <header>
                                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/">Nekrosys</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898058633"><i class="icon-forward" title="in reply to"></i> Tiredman</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898092831" title="Tuesday, March 10, 2015 9:39 AM">a day ago</a></span>
                                            </header>

                                            <div class="post-body-inner">
                                                <div class="post-message-container" data-role="message-container">
                                                    <div class="publisher-anchor-color" data-role="message-content">
                                                        <div class="post-message" data-role="message" dir="auto">
                                                            <p>Well there may also be cultural differences.</p>

                                                            <p>See, I do think a lot of horror stories of cops get latched on to by media outlets just because it allows for a good (read: profitable) story. While there are without a doubt cops of ill-intent, I would assume (read: hope like hell) that they're few and far-between. Though there are the occasional stories over here of cops using their guns as sex toys (that actually happened a month or two ago - it was weird).</p>

                                                            <p>As is, most of the 'horror stories' I've heard first-hand about cops over here (Australia, so again, cultural differences) are more stories of people being in the wrong and throwing a fit about it because they got caught speeding or some stupid shit along those lines.</p>
                                                        </div><span class="post-media"></span>

                                                        <ul data-role="post-media-list"></ul>
                                                    </div>
                                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                            </div>

                                            <footer>
                                                <ul>
                                                    <li class="voting" data-role="voting">
                                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="reply" data-role="reply-link">
                                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="share">
                                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                        <ul>
                                                            <li class="twitter">
                                                                <a data-action="share:twitter" href="#">Twitter</a>
                                                            </li>

                                                            <li class="facebook">
                                                                <a data-action="share:facebook" href="#">Facebook</a>
                                                            </li>

                                                            <li class="link">
                                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898092831">Link</a>
                                                            </li>
                                                        </ul>
                                                    </li>

                                                    <li class="realtime" data-role="realtime-notification:1898092831">
                                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                    </li>
                                                </ul>
                                            </footer>
                                        </div>

                                        <div data-role="blacklist-form"></div>

                                        <div class="reply-form-container" data-role="reply-form"></div>
                                    </div>

                                    <ul class="children" data-role="children">
                                        <li class="post" id="post-1898105608">
                                            <div></div>

                                            <div class="post-content" data-role="post-content">
                                                <ul class="post-menu dropdown" data-role="menu">
                                                    <li class="collapse">
                                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                                    </li>

                                                    <li class="expand">
                                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                                    </li>

                                                    <li class="">
                                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                                    </li>
                                                </ul>

                                                <div class="indicator"></div>

                                                <div class="avatar hovercard">
                                                    <a class="user" data-action="profile" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/"><img alt="Avatar" data-role="user-avatar" data-user="51506332" src="//a.disquscdn.com/uploads/users/5150/6332/avatar92.jpg?1369207961"></a>
                                                </div>

                                                <div class="post-body">
                                                    <header>
                                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/">Tiredman</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898092831"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898105608" title="Tuesday, March 10, 2015 9:49 AM">a day ago</a></span>
                                                    </header>

                                                    <div class="post-body-inner">
                                                        <div class="post-message-container" data-role="message-container">
                                                            <div class="publisher-anchor-color" data-role="message-content">
                                                                <div class="post-message" data-role="message" dir="auto">
                                                                    <p>You see, the stories have to happen to be reported on, otherwise those places would get sued into dust. That is the problem now. With the internet and cell phones, cop abuse no longer stays between the cops and the victim. Yes cops have a hard job, but they shouldn't be allowed to take out their stress on the innocent.</p>

                                                                    <p>And aye, my family are located in the mountains of Eastern Kentucky, bible belt country. The town I am living in right now only has a population of 3600, with many of the surrounding small towns being even smaller. Moved here a few years ago, and now I am counting the minutes till I can move away, hopefully sometime this year.</p>
                                                                </div><span class="post-media"></span>

                                                                <ul data-role="post-media-list"></ul>
                                                            </div>
                                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                                    </div>

                                                    <footer>
                                                        <ul>
                                                            <li class="voting" data-role="voting">
                                                                <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="reply" data-role="reply-link">
                                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="share">
                                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                                <ul>
                                                                    <li class="twitter">
                                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                                    </li>

                                                                    <li class="facebook">
                                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                                    </li>

                                                                    <li class="link">
                                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898105608">Link</a>
                                                                    </li>
                                                                </ul>
                                                            </li>

                                                            <li class="realtime" data-role="realtime-notification:1898105608">
                                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                            </li>
                                                        </ul>
                                                    </footer>
                                                </div>

                                                <div data-role="blacklist-form"></div>

                                                <div class="reply-form-container" data-role="reply-form"></div>
                                            </div>

                                            <ul class="children" data-role="children">
                                                <li class="post" id="post-1898122053">
                                                    <div></div>

                                                    <div class="post-content" data-role="post-content">
                                                        <ul class="post-menu dropdown" data-role="menu">
                                                            <li class="collapse">
                                                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                                            </li>

                                                            <li class="expand">
                                                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                                            </li>

                                                            <li class="">
                                                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                                            </li>
                                                        </ul>

                                                        <div class="indicator"></div>

                                                        <div class="avatar hovercard">
                                                            <a class="user" data-action="profile" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/"><img alt="Avatar" data-role="user-avatar" data-user="104252315" src="//a.disquscdn.com/uploads/users/10425/2315/avatar92.jpg?1425200107"></a>
                                                        </div>

                                                        <div class="post-body">
                                                            <header>
                                                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/">Nekrosys</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898105608"><i class="icon-forward" title="in reply to"></i> Tiredman</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898122053" title="Tuesday, March 10, 2015 10:02 AM">a day ago</a></span>
                                                            </header>

                                                            <div class="post-body-inner">
                                                                <div class="post-message-container" data-role="message-container" style="height: 374px;">
                                                                    <div class="publisher-anchor-color" data-role="message-content">
                                                                        <div class="post-message" data-role="message" dir="auto">
                                                                            <p>Yeah, but I mean, for every "cop does evil shit" story, there's likely to be thousands of "cop does good shit" stories that won't be reported on by the media. Naturally, people see more bad-cop stories than good-cop ones. That's just the way media works. Not to mention I don't believe many people will be filming cops if they're doing their jobs properly. Though without a doubt they'll have their phones out if a cop misbehaves.</p>

                                                                            <p>All of that can lead to a slightly skewed picture with regards to actual police brutality. We're quicker to latch on to the negatives rather than the positives.</p>

                                                                            <p>Without a doubt, there are cops that aren't doing the right thing. And they should be dealt with accordingly. But I do genuinely think that most of them have the right idea. Or at least, that's what I've personally seen a lot more of.</p>

                                                                            <p>That may be because where I live just doesn't have as much violent crime. So I guess our police force just aren't as on-edge as they are in a country where dangerous weapons are readily available (pardon for getting a little political with regards to guns). That may be a contributing factor.</p>

                                                                            <p>Now I do think that if a cop commits a violent crime, they should be dealt with. I also think that police should be held to much greater accountability than most of the populace, considering these people are meant to protect the people and serve as an example. But I do not think that the majority are corrupt.</p>
                                                                        </div><span class="post-media"></span>

                                                                        <ul data-role="post-media-list"></ul>
                                                                    </div>
                                                                </div><a class="see-more" data-action="see-more" title="see more">see more</a>
                                                            </div>

                                                            <footer>
                                                                <ul>
                                                                    <li class="voting" data-role="voting">
                                                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                                    </li>

                                                                    <li class="bullet">•</li>

                                                                    <li class="reply" data-role="reply-link">
                                                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                                    </li>

                                                                    <li class="bullet">•</li>

                                                                    <li class="share">
                                                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                                        <ul>
                                                                            <li class="twitter">
                                                                                <a data-action="share:twitter" href="#">Twitter</a>
                                                                            </li>

                                                                            <li class="facebook">
                                                                                <a data-action="share:facebook" href="#">Facebook</a>
                                                                            </li>

                                                                            <li class="link">
                                                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898122053">Link</a>
                                                                            </li>
                                                                        </ul>
                                                                    </li>

                                                                    <li class="realtime" data-role="realtime-notification:1898122053">
                                                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                                    </li>
                                                                </ul>
                                                            </footer>
                                                        </div>

                                                        <div data-role="blacklist-form"></div>

                                                        <div class="reply-form-container" data-role="reply-form"></div>
                                                    </div>

                                                    <ul class="children" data-role="children">
                                                        <li class="post" id="post-1898266925">
                                                            <div></div>

                                                            <div class="post-content" data-role="post-content">
                                                                <ul class="post-menu dropdown" data-role="menu">
                                                                    <li class="collapse">
                                                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                                                    </li>

                                                                    <li class="expand">
                                                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                                                    </li>

                                                                    <li class="">
                                                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                                                    </li>
                                                                </ul>

                                                                <div class="indicator"></div>

                                                                <div class="avatar hovercard">
                                                                    <a class="user" data-action="profile" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/"><img alt="Avatar" data-role="user-avatar" data-user="51506332" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                                                </div>

                                                                <div class="post-body">
                                                                    <header>
                                                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/">Tiredman</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898122053"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898266925" title="Tuesday, March 10, 2015 12:20 PM">a day ago</a></span>
                                                                    </header>

                                                                    <div class="post-body-inner">
                                                                        <div class="post-message-container" data-role="message-container">
                                                                            <div class="publisher-anchor-color" data-role="message-content">
                                                                                <div class="post-message" data-role="message" dir="auto">
                                                                                    <p>What it all boils down to is the police need stricter standards of hiring. Also they need to up their game to get these issues stopped, preferably before they happen through psych evaluations and training. Even if it is only a handful of bad apples, they are dealing with people's lives, which makes it a huge problem when one of those few bad things happen.</p>

                                                                                    <p>The last thing is, as you say, if a cop does a violent crime, they should be dealt with. We are having an issue at the moment where the corruption is showing in the lime light. In the US its knowing that lawyers and judges will protect the police force, even when the police are in the wrong. A new story recently talked about a lawyer in an area who actually went against a cop in that same area.</p>

                                                                                    <p>After the trial, which I can't remember if it was a win or a loss for the lawyer, the police force in mass started not participating with the justice department on crimes, and making the job harder for that lawyer and others who were buddies with that lawyer. That is a serious problem. When the police protect those who broke the law, even when they know that cop broke the law, it shows how deep the corruption has gone. And even when judges and lawyers get in on it, then justice truly is blind because it can't tell when it is being abused.</p>
                                                                                </div><span class="post-media"></span>

                                                                                <ul data-role="post-media-list"></ul>
                                                                            </div>
                                                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                                                    </div>

                                                                    <footer>
                                                                        <ul>
                                                                            <li class="voting" data-role="voting">
                                                                                <a class="vote-up count-2" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">2</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                                            </li>

                                                                            <li class="bullet">•</li>

                                                                            <li class="reply" data-role="reply-link">
                                                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                                            </li>

                                                                            <li class="bullet">•</li>

                                                                            <li class="share">
                                                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                                                <ul>
                                                                                    <li class="twitter">
                                                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                                                    </li>

                                                                                    <li class="facebook">
                                                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                                                    </li>

                                                                                    <li class="link">
                                                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898266925">Link</a>
                                                                                    </li>
                                                                                </ul>
                                                                            </li>

                                                                            <li class="realtime" data-role="realtime-notification:1898266925">
                                                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                                            </li>
                                                                        </ul>
                                                                    </footer>
                                                                </div>

                                                                <div data-role="blacklist-form"></div>

                                                                <div class="reply-form-container" data-role="reply-form"></div>
                                                            </div>

                                                            <ul class="children" data-role="children"></ul>
                                                        </li>
                                                    </ul>
                                                </li>
                                            </ul>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>

                <li class="post" id="post-1896334848">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="Beoslasher" href="https://disqus.com/by/Beoslasher/"><img alt="Avatar" data-role="user-avatar" data-user="66156770" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Beoslasher" href="https://disqus.com/by/Beoslasher/">Miles Wilburn</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896305588"><i class="icon-forward" title="in reply to"></i> Devin Lee</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896334848" title="Monday, March 9, 2015 7:16 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>Unfortunately, these shooting cases are probably more than just asshole cops shooting people for no reason. The media is gonna portray whatever side will get them the most ratings. The mistake people make is that they think media sources are their friends. However, in this case it's cut and dry and its a damn shame that the officer had to be killed. Hope these criminals get their just desserts.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-6" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">6</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-3" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896334848">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896334848">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children">
                        <li class="post" id="post-1896972779">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="modernmethod-05f747f9753a0b4172a8faf1128a78e1" href="https://disqus.com/by/modernmethod-05f747f9753a0b4172a8faf1128a78e1/"><img alt="Avatar" data-role="user-avatar" data-user="34194483" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-05f747f9753a0b4172a8faf1128a78e1" href="https://disqus.com/by/modernmethod-05f747f9753a0b4172a8faf1128a78e1/">Retrofraction</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896334848"><i class="icon-forward" title="in reply to"></i> Miles Wilburn</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896972779" title="Tuesday, March 10, 2015 12:28 AM">a day ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>It is so true, most media corporations are owned by banks... and rather focus on news to better themselves.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896972779">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1896972779">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children"></ul>
                        </li>

                        <li class="post" id="post-1897052828">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="disqus_fq3Dz51T3b" href="https://disqus.com/by/disqus_fq3Dz51T3b/"><img alt="Avatar" data-role="user-avatar" data-user="96832845" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="disqus_fq3Dz51T3b" href="https://disqus.com/by/disqus_fq3Dz51T3b/">bob loblaw</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896334848"><i class="icon-forward" title="in reply to"></i> Miles Wilburn</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1897052828" title="Tuesday, March 10, 2015 12:58 AM">a day ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>Its easy to say not being a cop. Have a job where getting shot is a daily possibility, then see how you react to someone who charges you and goes for your gun, or makes a stupid quick motion with their hand from their belt.<br>
                                                    Very easy to say its just cops being assholes and shooting people because of color. Completely different reality when you are a cop and losing you life earning a middle class salary is a real possibility.<br>
                                                    Im sure if you ask any cop involved in recent shooting, they all would have preferred things didn't go that way, but I guarantee you you wouldn't be ready to sacrifice your life in the name of social justice.<br>
                                                    If you ask me, how stupid does someone have to be to either charge a cop with his gun drawn, or not follow the simple orders a cop gives you when they approach you with a gun drawn? Cops doesn't know you, who you are, what you have on you, or your intent. Just play along put your hand up and let the cop determine you are no threat and no one gets shot.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1897052828">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1897052828">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children">
                                <li class="post" id="post-1898066378">
                                    <div></div>

                                    <div class="post-content" data-role="post-content">
                                        <ul class="post-menu dropdown" data-role="menu">
                                            <li class="collapse">
                                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                            </li>

                                            <li class="expand">
                                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                            </li>

                                            <li class="">
                                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                            </li>
                                        </ul>

                                        <div class="indicator"></div>

                                        <div class="avatar hovercard">
                                            <a class="user" data-action="profile" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/"><img alt="Avatar" data-role="user-avatar" data-user="51506332" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                        </div>

                                        <div class="post-body">
                                            <header>
                                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/">Tiredman</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1897052828"><i class="icon-forward" title="in reply to"></i> bob loblaw</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898066378" title="Tuesday, March 10, 2015 9:20 AM">a day ago</a></span>
                                            </header>

                                            <div class="post-body-inner">
                                                <div class="post-message-container" data-role="message-container">
                                                    <div class="publisher-anchor-color" data-role="message-content">
                                                        <div class="post-message" data-role="message" dir="auto">
                                                            <p>Watch the video on the hispanic man who was shot in Washington. That is why people are spooked by police. If you find the unedited video, you hear of a man throwing small rocks at police. Then police draw guns after a taser didn't work, and when the man is running across a road, the police open fire on him on a crowded street where their bullets could easily hit innocent bystanders. Then the police crossed the street after the man who had fallen do his knees. He held his arms up to the police who were hovering over him and finished him off execution style. A man was throwing rocks, and in return 3 or 4 cops filled him full of bullets.</p>

                                                            <p>The problem is that is not an isolated story thanks to mobile phones and the internet. Actually, that isn't a problem, that is a good thing that will hopefully cause the police force to start screening who it lets in and gives a license to kill. Too many power hungry people who have bully tendencies get into law enforcement just so they can be state backed bully's.</p>
                                                        </div><span class="post-media"></span>

                                                        <ul data-role="post-media-list"></ul>
                                                    </div>
                                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                            </div>

                                            <footer>
                                                <ul>
                                                    <li class="voting" data-role="voting">
                                                        <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="reply" data-role="reply-link">
                                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="share">
                                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                        <ul>
                                                            <li class="twitter">
                                                                <a data-action="share:twitter" href="#">Twitter</a>
                                                            </li>

                                                            <li class="facebook">
                                                                <a data-action="share:facebook" href="#">Facebook</a>
                                                            </li>

                                                            <li class="link">
                                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898066378">Link</a>
                                                            </li>
                                                        </ul>
                                                    </li>

                                                    <li class="realtime" data-role="realtime-notification:1898066378">
                                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                    </li>
                                                </ul>
                                            </footer>
                                        </div>

                                        <div data-role="blacklist-form"></div>

                                        <div class="reply-form-container" data-role="reply-form"></div>
                                    </div>

                                    <ul class="children" data-role="children"></ul>
                                </li>
                            </ul>
                        </li>

                        <li class="post" id="post-1898059462">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/"><img alt="Avatar" data-role="user-avatar" data-user="51506332" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="disqus_gwRZGkQcwi" href="https://disqus.com/by/disqus_gwRZGkQcwi/">Tiredman</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896334848"><i class="icon-forward" title="in reply to"></i> Miles Wilburn</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898059462" title="Tuesday, March 10, 2015 9:15 AM">a day ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>First degree murder, yeah, they will either get life without parole or death sentence if they are in a state with it.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898059462">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1898059462">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children"></ul>
                        </li>
                    </ul>
                </li>

                <li class="post" id="post-1896431132">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="modernmethod-84f44305ddacdb3c69e8aaf21312b343" href="https://disqus.com/by/modernmethod-84f44305ddacdb3c69e8aaf21312b343/"><img alt="Avatar" data-role="user-avatar" data-user="48332509" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-84f44305ddacdb3c69e8aaf21312b343" href="https://disqus.com/by/modernmethod-84f44305ddacdb3c69e8aaf21312b343/">Keiichi Morisato</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896305588"><i class="icon-forward" title="in reply to"></i> Devin Lee</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896431132" title="Monday, March 9, 2015 8:34 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>actually, in one of the cases that you are thinking of *chough* Ferguson *cough* the sole eyewitness lied because she beforehand already had a bias against police officers.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896431132">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896431132">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children"></ul>
                </li>

                <li class="post" id="post-1896604100">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="the_ferginator" href="https://disqus.com/by/the_ferginator/"><img alt="Avatar" data-role="user-avatar" data-user="48323331" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="the_ferginator" href="https://disqus.com/by/the_ferginator/">The Ferginator</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896305588"><i class="icon-forward" title="in reply to"></i> Devin Lee</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896604100" title="Monday, March 9, 2015 9:47 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container" style="height: 374px;">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p><span></span></p>

                                            <div class="media-container media-mode-deferred">
                                                <a class="media-button media-button-expand publisher-color publisher-border-color" data-action="expand" href="https://www.facebook.com/video.php?v=2296766557537&amp;pnref=storyhttps://www.facebook.com/video.php?v=2296766557537&amp;pnref=story" rel="nofollow" target="_blank" title="Facebook – Jerry LLanes | Facebook"><i class="icon-video publisher-background-color"></i> View</a> <a class="media-button media-button-contract publisher-color publisher-border-color" data-action="contract" href="#" target="_blank"><i class="icon-cancel publisher-background-color"></i> Hide</a>

                                                <div class="media-content-loader" data-role="content-loader"></div>

                                                <div class="media-content-placeholder" data-role="content-placeholder" style="height: 384px;">
                                                    <a class="media-force-load icon-video" data-action="force-load" href="#" style="font-style: italic"></a>
                                                </div>
                                            </div>
                                            <p>

                                            <p>I'm not condoning incidents like the Tamir Rice shooting, obviously that was just bullshit, but when you see what they have to put up with a lot of the time is it really that surprising when these things happen from time to time? Anyone who thinks the Ferguson riots were justified or has a mentality that thinks cop killing is justified by isolated incidents or even that these incidents reflect law enforcement as a whole, can go fuck themselves as far as i'm concerned.</p>

                                            <p>R.I.P. Brother.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-4" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">4</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896604100">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896604100">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children"></ul>
                </li>
            </ul>
        </li>

        <li class="post" id="post-1896306633">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="modernmethod-945201efd3c41709a17cfd4ee2eb0f81" href="https://disqus.com/by/modernmethod-945201efd3c41709a17cfd4ee2eb0f81/"><img alt="Avatar" data-role="user-avatar" data-user="31405479" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-945201efd3c41709a17cfd4ee2eb0f81" href="https://disqus.com/by/modernmethod-945201efd3c41709a17cfd4ee2eb0f81/">Osaka</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896306633" title="Monday, March 9, 2015 6:42 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>Hipps.</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896306633">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896306633">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children"></ul>
        </li>

        <li class="post" id="post-1896307060">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/"><img alt="Avatar" data-role="user-avatar" data-user="104252315" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/">Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896307060" title="Monday, March 9, 2015 6:43 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>Would now be the right time to make a comment about Amiibo being in low supply?</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896307060">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896307060">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children">
                <li class="post" id="post-1896310939">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="modernmethod-73043400d135f80e05f12572b60b2b17" href="https://disqus.com/by/modernmethod-73043400d135f80e05f12572b60b2b17/"><img alt="Avatar" data-role="user-avatar" data-user="102066339" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-73043400d135f80e05f12572b60b2b17" href="https://disqus.com/by/modernmethod-73043400d135f80e05f12572b60b2b17/">JBroXNari99</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896307060"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896310939" title="Monday, March 9, 2015 6:48 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>If a rare Amiibo came out today, that would have been terrible. The folks in New England are having to go out in freezing cold temperatures in the morning of they even want a chance of finding a rare, and now this happens? If he wanted to get him an Amiibo, that would have been terrible.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896310939">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896310939">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children"></ul>
                </li>

                <li class="post" id="post-1896835423">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="modernmethod-6ae650374b519325eb34d8187f5aa757" href="https://disqus.com/by/modernmethod-6ae650374b519325eb34d8187f5aa757/"><img alt="Avatar" data-role="user-avatar" data-user="38215922" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-6ae650374b519325eb34d8187f5aa757" href="https://disqus.com/by/modernmethod-6ae650374b519325eb34d8187f5aa757/">BlunderBuss</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896307060"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896835423" title="Monday, March 9, 2015 11:49 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>Not really, those things are worthless enough as it is.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896835423">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896835423">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children"></ul>
                </li>
            </ul>
        </li>

        <li class="post" id="post-1896311806">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="michaelrabattino" href="https://disqus.com/by/michaelrabattino/"><img alt="Avatar" data-role="user-avatar" data-user="55669613" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="michaelrabattino" href="https://disqus.com/by/michaelrabattino/">Michael Rabattino</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896311806" title="Monday, March 9, 2015 6:48 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>Hate to be this guy, but...*Philadelphia</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896311806">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896311806">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children">
                <li class="post" id="post-1896601400">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="modernmethod-8702581b10fc44c8ee9021a967744624" href="https://disqus.com/by/modernmethod-8702581b10fc44c8ee9021a967744624/"><img alt="Avatar" data-role="user-avatar" data-user="34193529" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-8702581b10fc44c8ee9021a967744624" href="https://disqus.com/by/modernmethod-8702581b10fc44c8ee9021a967744624/">Charlietime</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896311806"><i class="icon-forward" title="in reply to"></i> Michael Rabattino</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896601400" title="Monday, March 9, 2015 9:46 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>Philly is a great place, just don't go across the river unless you have to.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896601400">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896601400">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children">
                        <li class="post" id="post-1896739572">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="michaelrabattino" href="https://disqus.com/by/michaelrabattino/"><img alt="Avatar" data-role="user-avatar" data-user="55669613" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="michaelrabattino" href="https://disqus.com/by/michaelrabattino/">Michael Rabattino</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896601400"><i class="icon-forward" title="in reply to"></i> Charlietime</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896739572" title="Monday, March 9, 2015 11:13 PM">2 days ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>I live in South Jersey so I'm quite familiar with the greatness of Philly.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896739572">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1896739572">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children">
                                <li class="post" id="post-1898213857">
                                    <div></div>

                                    <div class="post-content" data-role="post-content">
                                        <ul class="post-menu dropdown" data-role="menu">
                                            <li class="collapse">
                                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                            </li>

                                            <li class="expand">
                                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                            </li>

                                            <li class="">
                                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                            </li>
                                        </ul>

                                        <div class="indicator"></div>

                                        <div class="avatar hovercard">
                                            <a class="user" data-action="profile" data-username="modernmethod-8702581b10fc44c8ee9021a967744624" href="https://disqus.com/by/modernmethod-8702581b10fc44c8ee9021a967744624/"><img alt="Avatar" data-role="user-avatar" data-user="34193529" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                        </div>

                                        <div class="post-body">
                                            <header>
                                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-8702581b10fc44c8ee9021a967744624" href="https://disqus.com/by/modernmethod-8702581b10fc44c8ee9021a967744624/">Charlietime</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896739572"><i class="icon-forward" title="in reply to"></i> Michael Rabattino</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898213857" title="Tuesday, March 10, 2015 11:20 AM">a day ago</a></span>
                                            </header>

                                            <div class="post-body-inner">
                                                <div class="post-message-container" data-role="message-container">
                                                    <div class="publisher-anchor-color" data-role="message-content">
                                                        <div class="post-message" data-role="message" dir="auto">
                                                            <p>then you've crossed the river and done fucked up. My misses is from cherry hill and I lived in lindenwold for a bit.</p>
                                                        </div><span class="post-media"></span>

                                                        <ul data-role="post-media-list"></ul>
                                                    </div>
                                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                            </div>

                                            <footer>
                                                <ul>
                                                    <li class="voting" data-role="voting">
                                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="reply" data-role="reply-link">
                                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="share">
                                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                        <ul>
                                                            <li class="twitter">
                                                                <a data-action="share:twitter" href="#">Twitter</a>
                                                            </li>

                                                            <li class="facebook">
                                                                <a data-action="share:facebook" href="#">Facebook</a>
                                                            </li>

                                                            <li class="link">
                                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1898213857">Link</a>
                                                            </li>
                                                        </ul>
                                                    </li>

                                                    <li class="realtime" data-role="realtime-notification:1898213857">
                                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                    </li>
                                                </ul>
                                            </footer>
                                        </div>

                                        <div data-role="blacklist-form"></div>

                                        <div class="reply-form-container" data-role="reply-form"></div>
                                    </div>

                                    <ul class="children" data-role="children"></ul>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </li>

                <li class="post" id="post-1896605514">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="CaptainProtonX" href="https://disqus.com/by/CaptainProtonX/"><img alt="Avatar" data-role="user-avatar" data-user="35032243" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="CaptainProtonX" href="https://disqus.com/by/CaptainProtonX/">CaptainProtonX</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896311806"><i class="icon-forward" title="in reply to"></i> Michael Rabattino</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896605514" title="Monday, March 9, 2015 9:48 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>Philadelphia is a metropolitan center with over 1.5 million residents. It is experiencing a massive dip in crime, and is seeing a rise in equity.</p>

                                            <p>Like any major city, it will experience crime as opportunists will take advantage of situations they feel will lead to a payoff. Blaming the situation on the city being a city is a vacuous argument and brings nothing to the topic of a brave individual dying in the line of fire.</p>

                                            <p>Hate to be this guy, but...*Troll.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896605514">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896605514">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children">
                        <li class="post" id="post-1896736634">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="michaelrabattino" href="https://disqus.com/by/michaelrabattino/"><img alt="Avatar" data-role="user-avatar" data-user="55669613" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="michaelrabattino" href="https://disqus.com/by/michaelrabattino/">Michael Rabattino</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896605514"><i class="icon-forward" title="in reply to"></i> CaptainProtonX</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896736634" title="Monday, March 9, 2015 11:12 PM">2 days ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>What the hell are you talking about? I was referring to the author's gross misspelling of the name of the city. It's been fixed since I posted, but it was "Philidelphia" before.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-2" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">2</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896736634">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1896736634">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children"></ul>
                        </li>
                    </ul>
                </li>
            </ul>
        </li>

        <li class="post" id="post-1896323246">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="S_Daedalus" href="https://disqus.com/by/S_Daedalus/"><img alt="Avatar" data-role="user-avatar" data-user="37813913" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="S_Daedalus" href="https://disqus.com/by/S_Daedalus/">S_Daedalus</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896323246" title="Monday, March 9, 2015 7:01 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>Madness...</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-2" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">2</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896323246">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896323246">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children"></ul>
        </li>

        <li class="post" id="post-1896325736">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="dieger" href="https://disqus.com/by/dieger/"><img alt="Avatar" data-role="user-avatar" data-user="39073275" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="dieger" href="https://disqus.com/by/dieger/">dieger</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896325736" title="Monday, March 9, 2015 7:04 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>shit ;/</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896325736">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896325736">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children"></ul>
        </li>

        <li class="post" id="post-1896337348">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="ThePerro" href="https://disqus.com/by/ThePerro/"><img alt="Avatar" data-role="user-avatar" data-user="96350405" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="ThePerro" href="https://disqus.com/by/ThePerro/">Perro</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896337348" title="Monday, March 9, 2015 7:19 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>So senseless, I hope for the best for his family during this hard time.</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-2" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">2</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896337348">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896337348">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children"></ul>
        </li>

        <li class="post" id="post-1896337645">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="disqus_gzIN10nmNv" href="https://disqus.com/by/disqus_gzIN10nmNv/"><img alt="Avatar" data-role="user-avatar" data-user="80723001" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="disqus_gzIN10nmNv" href="https://disqus.com/by/disqus_gzIN10nmNv/">EGG™</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896337645" title="Monday, March 9, 2015 7:20 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>That's so petty I hate it</p>

                                    <p>Why didnt they</p>

                                    <p>yknow</p>

                                    <p>try to rob another day?</p>

                                    <p>it doesnt solve the problem but any normal human being with common sense wouldve been scared and fleed instead of come up with lets get in a giant shootout with the cop over gamestop money</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896337645">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896337645">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children">
                <li class="post" id="post-1896351646">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="modernmethod-1d971eb3ba4f14c10bd64455b86b89aa" href="https://disqus.com/by/modernmethod-1d971eb3ba4f14c10bd64455b86b89aa/"><img alt="Avatar" data-role="user-avatar" data-user="38909424" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-1d971eb3ba4f14c10bd64455b86b89aa" href="https://disqus.com/by/modernmethod-1d971eb3ba4f14c10bd64455b86b89aa/">Chist</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896337645"><i class="icon-forward" title="in reply to"></i> EGG™</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896351646" title="Monday, March 9, 2015 7:36 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>Any crime that results in the loss of a life is petty. Nothing is worth that price.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-3" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">3</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896351646">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896351646">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children"></ul>
                </li>
            </ul>
        </li>

        <li class="post" id="post-1896338816">
            <div></div>

            <div class="post-content" data-role="post-content">
                <ul class="post-menu dropdown" data-role="menu">
                    <li class="collapse">
                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                    </li>

                    <li class="expand">
                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                    </li>

                    <li class="">
                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                    </li>
                </ul>

                <div class="indicator"></div>

                <div class="avatar hovercard">
                    <a class="user" data-action="profile" data-username="modernmethod-1d971eb3ba4f14c10bd64455b86b89aa" href="https://disqus.com/by/modernmethod-1d971eb3ba4f14c10bd64455b86b89aa/"><img alt="Avatar" data-role="user-avatar" data-user="38909424" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                </div>

                <div class="post-body">
                    <header>
                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-1d971eb3ba4f14c10bd64455b86b89aa" href="https://disqus.com/by/modernmethod-1d971eb3ba4f14c10bd64455b86b89aa/">Chist</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896338816" title="Monday, March 9, 2015 7:21 PM">2 days ago</a></span>
                    </header>

                    <div class="post-body-inner">
                        <div class="post-message-container" data-role="message-container">
                            <div class="publisher-anchor-color" data-role="message-content">
                                <div class="post-message" data-role="message" dir="auto">
                                    <p>This is an inappropriate article to be cracking jokes on, guys. Let's set aside the sarcasm and funny bone, guy was a badass and a hero, so just take the time to show him some respect, and appreciate the kind of danger he put himself in to keep civilians out of the crossfire.</p>
                                </div><span class="post-media"></span>

                                <ul data-role="post-media-list"></ul>
                            </div>
                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                    </div>

                    <footer>
                        <ul>
                            <li class="voting" data-role="voting">
                                <a class="vote-up count-65" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">65</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-2" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                            </li>

                            <li class="bullet">•</li>

                            <li class="reply" data-role="reply-link">
                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                            </li>

                            <li class="bullet">•</li>

                            <li class="share">
                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                <ul>
                                    <li class="twitter">
                                        <a data-action="share:twitter" href="#">Twitter</a>
                                    </li>

                                    <li class="facebook">
                                        <a data-action="share:facebook" href="#">Facebook</a>
                                    </li>

                                    <li class="link">
                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896338816">Link</a>
                                    </li>
                                </ul>
                            </li>

                            <li class="realtime" data-role="realtime-notification:1896338816">
                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                            </li>
                        </ul>
                    </footer>
                </div>

                <div data-role="blacklist-form"></div>

                <div class="reply-form-container" data-role="reply-form"></div>
            </div>

            <ul class="children" data-role="children">
                <li class="post" id="post-1896344471">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="modernmethod-97d0145823aeb8ed80617be62e08bdcc" href="https://disqus.com/by/modernmethod-97d0145823aeb8ed80617be62e08bdcc/"><img alt="Avatar" data-role="user-avatar" data-user="31411170" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-97d0145823aeb8ed80617be62e08bdcc" href="https://disqus.com/by/modernmethod-97d0145823aeb8ed80617be62e08bdcc/">pedrovay2003</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896338816"><i class="icon-forward" title="in reply to"></i> Chist</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896344471" title="Monday, March 9, 2015 7:28 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>That's not going to stop people, unfortunately, as we can already see.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896344471">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896344471">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children"></ul>
                </li>

                <li class="post" id="post-1896362061">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/"><img alt="Avatar" data-role="user-avatar" data-user="104252315" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/">Nekrosys</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896338816"><i class="icon-forward" title="in reply to"></i> Chist</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896362061" title="Monday, March 9, 2015 7:48 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>I'm probably an outlier here, but I'm very much of the impression that making a joke about a shitty situation can be used as a way to cheer oneself (and others - depending on the people) up just a little.</p>

                                            <p>You know, unless the joke is specifically targeted at the victim as a method of belittling them.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-12" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">12</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896362061">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896362061">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children">
                        <li class="post" id="post-1896363796">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="modernmethod-1d971eb3ba4f14c10bd64455b86b89aa" href="https://disqus.com/by/modernmethod-1d971eb3ba4f14c10bd64455b86b89aa/"><img alt="Avatar" data-role="user-avatar" data-user="38909424" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-1d971eb3ba4f14c10bd64455b86b89aa" href="https://disqus.com/by/modernmethod-1d971eb3ba4f14c10bd64455b86b89aa/">Chist</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896362061"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896363796" title="Monday, March 9, 2015 7:50 PM">2 days ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>No, I get it, it's fine to crack a joke in private, but this isn't the place for that kind of grieving.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-3" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896363796">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1896363796">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children">
                                <li class="post" id="post-1896459696">
                                    <div></div>

                                    <div class="post-content" data-role="post-content">
                                        <ul class="post-menu dropdown" data-role="menu">
                                            <li class="collapse">
                                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                            </li>

                                            <li class="expand">
                                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                            </li>

                                            <li class="">
                                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                            </li>
                                        </ul>

                                        <div class="indicator"></div>

                                        <div class="avatar hovercard">
                                            <a class="user" data-action="profile" data-username="modernmethod-73a492c854b0e4827cbd5684a8a5a076" href="https://disqus.com/by/modernmethod-73a492c854b0e4827cbd5684a8a5a076/"><img alt="Avatar" data-role="user-avatar" data-user="48333072" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                        </div>

                                        <div class="post-body">
                                            <header>
                                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-73a492c854b0e4827cbd5684a8a5a076" href="https://disqus.com/by/modernmethod-73a492c854b0e4827cbd5684a8a5a076/">whereismymind86</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896363796"><i class="icon-forward" title="in reply to"></i> Chist</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896459696" title="Monday, March 9, 2015 8:42 PM">2 days ago</a></span>
                                            </header>

                                            <div class="post-body-inner">
                                                <div class="post-message-container" data-role="message-container">
                                                    <div class="publisher-anchor-color" data-role="message-content">
                                                        <div class="post-message" data-role="message" dir="auto">
                                                            <p>shut the hell up, what makes you fucking special?</p>
                                                        </div><span class="post-media"></span>

                                                        <ul data-role="post-media-list"></ul>
                                                    </div>
                                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                            </div>

                                            <footer>
                                                <ul>
                                                    <li class="voting" data-role="voting">
                                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-4" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="reply" data-role="reply-link">
                                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="share">
                                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                        <ul>
                                                            <li class="twitter">
                                                                <a data-action="share:twitter" href="#">Twitter</a>
                                                            </li>

                                                            <li class="facebook">
                                                                <a data-action="share:facebook" href="#">Facebook</a>
                                                            </li>

                                                            <li class="link">
                                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896459696">Link</a>
                                                            </li>
                                                        </ul>
                                                    </li>

                                                    <li class="realtime" data-role="realtime-notification:1896459696">
                                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                    </li>
                                                </ul>
                                            </footer>
                                        </div>

                                        <div data-role="blacklist-form"></div>

                                        <div class="reply-form-container" data-role="reply-form"></div>
                                    </div>

                                    <ul class="children" data-role="children">
                                        <li class="post" id="post-1896461449">
                                            <div></div>

                                            <div class="post-content" data-role="post-content">
                                                <ul class="post-menu dropdown" data-role="menu">
                                                    <li class="collapse">
                                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                                    </li>

                                                    <li class="expand">
                                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                                    </li>

                                                    <li class="">
                                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                                    </li>
                                                </ul>

                                                <div class="indicator"></div>

                                                <div class="avatar hovercard">
                                                    <a class="user" data-action="profile" data-username="modernmethod-1d971eb3ba4f14c10bd64455b86b89aa" href="https://disqus.com/by/modernmethod-1d971eb3ba4f14c10bd64455b86b89aa/"><img alt="Avatar" data-role="user-avatar" data-user="38909424" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                                </div>

                                                <div class="post-body">
                                                    <header>
                                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-1d971eb3ba4f14c10bd64455b86b89aa" href="https://disqus.com/by/modernmethod-1d971eb3ba4f14c10bd64455b86b89aa/">Chist</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896459696"><i class="icon-forward" title="in reply to"></i> whereismymind86</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896461449" title="Monday, March 9, 2015 8:43 PM">2 days ago</a></span>
                                                    </header>

                                                    <div class="post-body-inner">
                                                        <div class="post-message-container" data-role="message-container">
                                                            <div class="publisher-anchor-color" data-role="message-content">
                                                                <div class="post-message" data-role="message" dir="auto">
                                                                    <p>Absolutely nothing. I'm just asking for some basic respect to be shown.</p>
                                                                </div><span class="post-media"></span>

                                                                <ul data-role="post-media-list"></ul>
                                                            </div>
                                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                                    </div>

                                                    <footer>
                                                        <ul>
                                                            <li class="voting" data-role="voting">
                                                                <a class="vote-up count-10" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">10</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="reply" data-role="reply-link">
                                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="share">
                                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                                <ul>
                                                                    <li class="twitter">
                                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                                    </li>

                                                                    <li class="facebook">
                                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                                    </li>

                                                                    <li class="link">
                                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896461449">Link</a>
                                                                    </li>
                                                                </ul>
                                                            </li>

                                                            <li class="realtime" data-role="realtime-notification:1896461449">
                                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                            </li>
                                                        </ul>
                                                    </footer>
                                                </div>

                                                <div data-role="blacklist-form"></div>

                                                <div class="reply-form-container" data-role="reply-form"></div>
                                            </div>

                                            <ul class="children" data-role="children"></ul>
                                        </li>

                                        <li class="post" id="post-1896471934">
                                            <div></div>

                                            <div class="post-content" data-role="post-content">
                                                <ul class="post-menu dropdown" data-role="menu">
                                                    <li class="collapse">
                                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                                    </li>

                                                    <li class="expand">
                                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                                    </li>

                                                    <li class="">
                                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                                    </li>
                                                </ul>

                                                <div class="indicator"></div>

                                                <div class="avatar hovercard">
                                                    <a class="user" data-action="profile" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/"><img alt="Avatar" data-role="user-avatar" data-user="104252315" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                                </div>

                                                <div class="post-body">
                                                    <header>
                                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/">Nekrosys</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896459696"><i class="icon-forward" title="in reply to"></i> whereismymind86</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896471934" title="Monday, March 9, 2015 8:52 PM">2 days ago</a></span>
                                                    </header>

                                                    <div class="post-body-inner">
                                                        <div class="post-message-container" data-role="message-container">
                                                            <div class="publisher-anchor-color" data-role="message-content">
                                                                <div class="post-message" data-role="message" dir="auto">
                                                                    <p>Disagree with Chist as much as you like, but that's a little bit unnecessarily harsh.</p>
                                                                </div><span class="post-media"></span>

                                                                <ul data-role="post-media-list"></ul>
                                                            </div>
                                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                                    </div>

                                                    <footer>
                                                        <ul>
                                                            <li class="voting" data-role="voting">
                                                                <a class="vote-up count-4" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">4</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="reply" data-role="reply-link">
                                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="share">
                                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                                <ul>
                                                                    <li class="twitter">
                                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                                    </li>

                                                                    <li class="facebook">
                                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                                    </li>

                                                                    <li class="link">
                                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896471934">Link</a>
                                                                    </li>
                                                                </ul>
                                                            </li>

                                                            <li class="realtime" data-role="realtime-notification:1896471934">
                                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                            </li>
                                                        </ul>
                                                    </footer>
                                                </div>

                                                <div data-role="blacklist-form"></div>

                                                <div class="reply-form-container" data-role="reply-form"></div>
                                            </div>

                                            <ul class="children" data-role="children"></ul>
                                        </li>

                                        <li class="post" id="post-1896477534">
                                            <div></div>

                                            <div class="post-content" data-role="post-content">
                                                <ul class="post-menu dropdown" data-role="menu">
                                                    <li class="collapse">
                                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                                    </li>

                                                    <li class="expand">
                                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                                    </li>

                                                    <li class="">
                                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                                    </li>
                                                </ul>

                                                <div class="indicator"></div>

                                                <div class="avatar hovercard">
                                                    <a class="user" data-action="profile" data-username="modernmethod-daed210307f1dbc6f1dd9551408d999f" href="https://disqus.com/by/modernmethod-daed210307f1dbc6f1dd9551408d999f/"><img alt="Avatar" data-role="user-avatar" data-user="34417113" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                                </div>

                                                <div class="post-body">
                                                    <header>
                                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-daed210307f1dbc6f1dd9551408d999f" href="https://disqus.com/by/modernmethod-daed210307f1dbc6f1dd9551408d999f/">JACK of No Trades</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896459696"><i class="icon-forward" title="in reply to"></i> whereismymind86</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896477534" title="Monday, March 9, 2015 8:55 PM">2 days ago</a></span>
                                                    </header>

                                                    <div class="post-body-inner">
                                                        <div class="post-message-container" data-role="message-container">
                                                            <div class="publisher-anchor-color" data-role="message-content">
                                                                <div class="post-message" data-role="message" dir="auto">
                                                                    <p>He is right, you are wrong. Deal with it punk.</p>
                                                                </div><span class="post-media"></span>

                                                                <ul data-role="post-media-list"></ul>
                                                            </div>
                                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                                    </div>

                                                    <footer>
                                                        <ul>
                                                            <li class="voting" data-role="voting">
                                                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="reply" data-role="reply-link">
                                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="share">
                                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                                <ul>
                                                                    <li class="twitter">
                                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                                    </li>

                                                                    <li class="facebook">
                                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                                    </li>

                                                                    <li class="link">
                                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896477534">Link</a>
                                                                    </li>
                                                                </ul>
                                                            </li>

                                                            <li class="realtime" data-role="realtime-notification:1896477534">
                                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                            </li>
                                                        </ul>
                                                    </footer>
                                                </div>

                                                <div data-role="blacklist-form"></div>

                                                <div class="reply-form-container" data-role="reply-form"></div>
                                            </div>

                                            <ul class="children" data-role="children"></ul>
                                        </li>

                                        <li class="post" id="post-1896712696">
                                            <div></div>

                                            <div class="post-content" data-role="post-content">
                                                <ul class="post-menu dropdown" data-role="menu">
                                                    <li class="collapse">
                                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                                    </li>

                                                    <li class="expand">
                                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                                    </li>

                                                    <li class="">
                                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                                    </li>
                                                </ul>

                                                <div class="indicator"></div>

                                                <div class="avatar hovercard">
                                                    <a class="user" data-action="profile" data-username="coppersam" href="https://disqus.com/by/coppersam/"><img alt="Avatar" data-role="user-avatar" data-user="117937138" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                                </div>

                                                <div class="post-body">
                                                    <header>
                                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="coppersam" href="https://disqus.com/by/coppersam/">coppersam</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896459696"><i class="icon-forward" title="in reply to"></i> whereismymind86</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896712696" title="Monday, March 9, 2015 10:59 PM">2 days ago</a></span>
                                                    </header>

                                                    <div class="post-body-inner">
                                                        <div class="post-message-container" data-role="message-container">
                                                            <div class="publisher-anchor-color" data-role="message-content">
                                                                <div class="post-message" data-role="message" dir="auto">
                                                                    <p>move along. come back in a few years when your maturity allows you to participate in social discourse like an adult.</p>
                                                                </div><span class="post-media"></span>

                                                                <ul data-role="post-media-list"></ul>
                                                            </div>
                                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                                    </div>

                                                    <footer>
                                                        <ul>
                                                            <li class="voting" data-role="voting">
                                                                <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="reply" data-role="reply-link">
                                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                            </li>

                                                            <li class="bullet">•</li>

                                                            <li class="share">
                                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                                <ul>
                                                                    <li class="twitter">
                                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                                    </li>

                                                                    <li class="facebook">
                                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                                    </li>

                                                                    <li class="link">
                                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896712696">Link</a>
                                                                    </li>
                                                                </ul>
                                                            </li>

                                                            <li class="realtime" data-role="realtime-notification:1896712696">
                                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                            </li>
                                                        </ul>
                                                    </footer>
                                                </div>

                                                <div data-role="blacklist-form"></div>

                                                <div class="reply-form-container" data-role="reply-form"></div>
                                            </div>

                                            <ul class="children" data-role="children"></ul>
                                        </li>
                                    </ul>
                                </li>
                            </ul>
                        </li>

                        <li class="post" id="post-1896426571">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="Absolutfreak" href="https://disqus.com/by/Absolutfreak/"><img alt="Avatar" data-role="user-avatar" data-user="27373701" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Absolutfreak" href="https://disqus.com/by/Absolutfreak/">Absolutfreak</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896362061"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896426571" title="Monday, March 9, 2015 8:30 PM">2 days ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>I agree with you, but generally the internet is the place where things get right out of hand.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-3" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">3</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896426571">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1896426571">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children"></ul>
                        </li>

                        <li class="post" id="post-1896553941">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="modernmethod-9b31229c5fd58c1ddb694f0232d0dd1f" href="https://disqus.com/by/modernmethod-9b31229c5fd58c1ddb694f0232d0dd1f/"><img alt="Avatar" data-role="user-avatar" data-user="31431672" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-9b31229c5fd58c1ddb694f0232d0dd1f" href="https://disqus.com/by/modernmethod-9b31229c5fd58c1ddb694f0232d0dd1f/">Ragnar Dragonfyre</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896362061"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896553941" title="Monday, March 9, 2015 9:20 PM">2 days ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>There are situations where you can make light of a shitty situation to cheer oneself up.</p>

                                                    <p>This is not one of them.</p>

                                                    <p>A man is dead. Show some fucking respect.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-3" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">3</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-1" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896553941">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1896553941">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children">
                                <li class="post" id="post-1896559709">
                                    <div></div>

                                    <div class="post-content" data-role="post-content">
                                        <ul class="post-menu dropdown" data-role="menu">
                                            <li class="collapse">
                                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                            </li>

                                            <li class="expand">
                                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                            </li>

                                            <li class="">
                                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                            </li>
                                        </ul>

                                        <div class="indicator"></div>

                                        <div class="avatar hovercard">
                                            <a class="user" data-action="profile" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/"><img alt="Avatar" data-role="user-avatar" data-user="104252315" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                        </div>

                                        <div class="post-body">
                                            <header>
                                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="Nekrosys" href="https://disqus.com/by/Nekrosys/">Nekrosys</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896553941"><i class="icon-forward" title="in reply to"></i> Ragnar Dragonfyre</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896559709" title="Monday, March 9, 2015 9:23 PM">2 days ago</a></span>
                                            </header>

                                            <div class="post-body-inner">
                                                <div class="post-message-container" data-role="message-container">
                                                    <div class="publisher-anchor-color" data-role="message-content">
                                                        <div class="post-message" data-role="message" dir="auto">
                                                            <p>That's a pretty disrespectful way of asking for respect, if I do say so myself.</p>

                                                            <p>Is that the way you speak to everyone with a difference of opinion?</p>
                                                        </div><span class="post-media"></span>

                                                        <ul data-role="post-media-list"></ul>
                                                    </div>
                                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                            </div>

                                            <footer>
                                                <ul>
                                                    <li class="voting" data-role="voting">
                                                        <a class="vote-up count-4" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">4</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-3" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="reply" data-role="reply-link">
                                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                                    </li>

                                                    <li class="bullet">•</li>

                                                    <li class="share">
                                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                        <ul>
                                                            <li class="twitter">
                                                                <a data-action="share:twitter" href="#">Twitter</a>
                                                            </li>

                                                            <li class="facebook">
                                                                <a data-action="share:facebook" href="#">Facebook</a>
                                                            </li>

                                                            <li class="link">
                                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896559709">Link</a>
                                                            </li>
                                                        </ul>
                                                    </li>

                                                    <li class="realtime" data-role="realtime-notification:1896559709">
                                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                                    </li>
                                                </ul>
                                            </footer>
                                        </div>

                                        <div data-role="blacklist-form"></div>

                                        <div class="reply-form-container" data-role="reply-form"></div>
                                    </div>

                                    <ul class="children" data-role="children"></ul>
                                </li>
                            </ul>
                        </li>

                        <li class="post" id="post-1897252124">
                            <div></div>

                            <div class="post-content" data-role="post-content">
                                <ul class="post-menu dropdown" data-role="menu">
                                    <li class="collapse">
                                        <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                                    </li>

                                    <li class="expand">
                                        <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                                    </li>

                                    <li class="">
                                        <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                                    </li>
                                </ul>

                                <div class="indicator"></div>

                                <div class="avatar hovercard">
                                    <a class="user" data-action="profile" data-username="modernmethod-cd9015a609618aa8dcd0a7ff7941c475" href="https://disqus.com/by/modernmethod-cd9015a609618aa8dcd0a7ff7941c475/"><img alt="Avatar" data-role="user-avatar" data-user="31592297" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                                </div>

                                <div class="post-body">
                                    <header>
                                        <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="modernmethod-cd9015a609618aa8dcd0a7ff7941c475" href="https://disqus.com/by/modernmethod-cd9015a609618aa8dcd0a7ff7941c475/">MuddBstrd</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896362061"><i class="icon-forward" title="in reply to"></i> Nekrosys</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1897252124" title="Tuesday, March 10, 2015 2:23 AM">a day ago</a></span>
                                    </header>

                                    <div class="post-body-inner">
                                        <div class="post-message-container" data-role="message-container">
                                            <div class="publisher-anchor-color" data-role="message-content">
                                                <div class="post-message" data-role="message" dir="auto">
                                                    <p>Dude, this isn't about cheering YOU up, it's about showing respect for someone else. By making the situation about what you want, you're being incredibly self-centered.</p>
                                                </div><span class="post-media"></span>

                                                <ul data-role="post-media-list"></ul>
                                            </div>
                                        </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                                    </div>

                                    <footer>
                                        <ul>
                                            <li class="voting" data-role="voting">
                                                <a class="vote-up count-1" data-action="upvote" href="#" title=""><span class="updatable count" data-role="likes">1</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="reply" data-role="reply-link">
                                                <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                            </li>

                                            <li class="bullet">•</li>

                                            <li class="share">
                                                <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                                <ul>
                                                    <li class="twitter">
                                                        <a data-action="share:twitter" href="#">Twitter</a>
                                                    </li>

                                                    <li class="facebook">
                                                        <a data-action="share:facebook" href="#">Facebook</a>
                                                    </li>

                                                    <li class="link">
                                                        <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1897252124">Link</a>
                                                    </li>
                                                </ul>
                                            </li>

                                            <li class="realtime" data-role="realtime-notification:1897252124">
                                                <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                            </li>
                                        </ul>
                                    </footer>
                                </div>

                                <div data-role="blacklist-form"></div>

                                <div class="reply-form-container" data-role="reply-form"></div>
                            </div>

                            <ul class="children" data-role="children"></ul>
                        </li>
                    </ul>
                </li>

                <li class="post" id="post-1896607633">
                    <div></div>

                    <div class="post-content" data-role="post-content">
                        <ul class="post-menu dropdown" data-role="menu">
                            <li class="collapse">
                                <a data-action="collapse" href="#" title="Collapse"><span>−</span></a>
                            </li>

                            <li class="expand">
                                <a data-action="collapse" href="#" title="Expand"><span>+</span></a>
                            </li>

                            <li class="">
                                <a class="dropdown-toggle icon icon-flag" data-action="flag" data-role="flag" href="#" style="font-style: italic" title="Flag as inappropriate"></a>
                            </li>
                        </ul>

                        <div class="indicator"></div>

                        <div class="avatar hovercard">
                            <a class="user" data-action="profile" data-username="KymikoLoco" href="https://disqus.com/by/KymikoLoco/"><img alt="Avatar" data-role="user-avatar" data-user="75932539" src="//a.disquscdn.com/uploads/forums/68/1221/avatar92.jpg?1387564011"></a>
                        </div>

                        <div class="post-body">
                            <header>
                                <span class="post-byline"><span class="author publisher-anchor-color"><a data-action="profile" data-role="username" data-username="KymikoLoco" href="https://disqus.com/by/KymikoLoco/">KymikoLoco</a></span> <span><a class="parent-link" data-role="parent-link" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896338816"><i class="icon-forward" title="in reply to"></i> Chist</a></span></span> <span class="post-meta"><span class="bullet time-ago-bullet">•</span> <a class="time-ago" data-role="relative-time" href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896607633" title="Monday, March 9, 2015 9:50 PM">2 days ago</a></span>
                            </header>

                            <div class="post-body-inner">
                                <div class="post-message-container" data-role="message-container">
                                    <div class="publisher-anchor-color" data-role="message-content">
                                        <div class="post-message" data-role="message" dir="auto">
                                            <p>Who was cracking jokes?</p>

                                            <p>Seriously, this is a featured comment, but I only saw one deleted comment that I presume was 'joking'.</p>

                                            <p>The featured comment should be the one about the fund set up for the officer's family.</p>
                                        </div><span class="post-media"></span>

                                        <ul data-role="post-media-list"></ul>
                                    </div>
                                </div><a class="see-more hidden" data-action="see-more" title="see more">see more</a>
                            </div>

                            <footer>
                                <ul>
                                    <li class="voting" data-role="voting">
                                        <a class="vote-up count-0" data-action="upvote" href="#" title="Vote up"><span class="updatable count" data-role="likes">0</span> <span class="control icon icon-arrow-2" style="font-style: italic"></span></a> <span class="vote-down count-0" data-action="downvote" title="Vote down"><span class="control icon icon-arrow" style="font-style: italic"></span></span>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="reply" data-role="reply-link">
                                        <a data-action="reply" href="#"><i class="icon icon-mobile icon-reply"></i><span class="text">Reply</span></a>
                                    </li>

                                    <li class="bullet">•</li>

                                    <li class="share">
                                        <a class="toggle"><i class="icon icon-mobile icon-share"></i><span class="text">Share ›</span></a>

                                        <ul>
                                            <li class="twitter">
                                                <a data-action="share:twitter" href="#">Twitter</a>
                                            </li>

                                            <li class="facebook">
                                                <a data-action="share:facebook" href="#">Facebook</a>
                                            </li>

                                            <li class="link">
                                                <a href="http://www.destructoid.com/police-officer-killed-during-gamestop-robbery-288794.phtml#comment-1896607633">Link</a>
                                            </li>
                                        </ul>
                                    </li>

                                    <li class="realtime" data-role="realtime-notification:1896607633">
                                        <span class="realtime-replies" style="display:none;"></span> <a class="btn btn-small" href="#" style="display:none;"></a>
                                    </li>
                                </ul>
                            </footer>
                        </div>

                        <div data-role="blacklist-form"></div>

                        <div class="reply-form-container" data-role="reply-form"></div>
                    </div>

                    <ul class="children" data-role="children"></ul>
                </li>
            </ul>
        </li>
    </ul>

    <div class="load-more" data-role="more" style="">
        <a class="btn" data-action="more-posts" href="#">Load more comments</a>
    </div>
</div>
''', 'lxml')
