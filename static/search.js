$(document).ready(function () {
    // alert("111")
    search_wd()

})
$(function() {
　　if (window.history && window.history.pushState) {
　　$(window).on('popstate', function () {
    　　window.location.reload()
　　});
　　}
    // alert("2")
　　})
jQuery.extend({highlight:function(a, j, g, f) {
    if (a.nodeType === 3) {
        var d = a.data.match(j);
        if (d && d[0].length) {
            var b = document.createElement(g || "span");
            b.className = f || "highlight";
            var h = a.splitText(d.index);
            h.splitText(d[0].length);
            var e = h.cloneNode(true);
            b.appendChild(e);
            h.parentNode.replaceChild(b, h);
            return 1
        }
    } else {
        if ((a.nodeType === 1 && a.childNodes) && !/(script|style)/i.test(a.tagName) && !(a.tagName === g.toUpperCase() && a.className === f)) {
            for (var c = 0; c < a.childNodes.length; c++) {
                c += jQuery.highlight(a.childNodes[c], j, g, f)
            }
        }
    }
    return 0
}});
jQuery.fn.unhighlight = function(a) {
    var b = {className:"keyword",element:"span"};
    jQuery.extend(b, a);
    return this.find(b.element + "." + b.className).each(
        function() {
            var c = this.parentNode;
            c.replaceChild(this.firstChild, this);
            c.normalize()
        }).end()
};
jQuery.fn.highlight = function(f, b) {
    var d = {className:"keyword",element:"span",caseSensitive:false,wordsOnly:false};
    jQuery.extend(d, b);
    if (f.constructor === String) {
        f = [f]
    }
    f = jQuery.grep(f, function(h, g) {
        return h != ""
    });

    if (f.length == 0) {
        return this
    }
    var a = d.caseSensitive ? "" : "i";
    var ea = [];
    $.each(f, function(i, ed) {
        ed = decodeURIComponent(ed);
        var eed = ed.replace(/([!~@`<>~！，。,.；;’'\[\]\/\\\?])/g, "\\$1");
        if (eed) {
            ea.push(eed);
        }
    });
    var e = "(" + ea.join("|") + ")";
    if (d.wordsOnly) {
        e = "\\b" + e + "\\b"
    }
    var c = new RegExp(e, a);
    return this.each(function() {
        jQuery.highlight(this, c, d.element, d.className)
    })
};
function createUrl(url) {
    var url_protocl=window.location.protocol;
    var domain = document.domain;
    var port = document.location.port;
    if (port=="80"){
        ab_url=url_protocl+"//"+domain+url;
    }else{
        ab_url=url_protocl+"//"+domain+":"+port+url;
    }

    return ab_url
}
function createNode(msg) {
    doc_id=msg[0];
    score=msg[1];
    textcut=msg[2];
    docs=msg[3];
    port=window.location.port;
    url="/docs?doc_id="+doc_id;
    ab_url=createUrl(url)

    node=$("<tr></tr>");
    node_title=$("<a></a>");
    node_title.attr('href',ab_url);
    node_title.attr('result_highlight','true');
    node_title.text(textcut);

    node.append(node_title);
    node_text=$("<div></div>");
    node_text.text(docs);
    node_text.attr('result_highlight','true');
    node_text.css("font-size","small");
    node_text.addClass("find_result");
    node.append(node_text);

    node_div=$("<div></div>");
    node_div.css("font-size","smaller");


    node_url=$("<a></a>");
    node_url.attr('href',ab_url);
    node_url.css('color',"green");
    node_url.text(ab_url);

    node_div.append(node_url);

    node_score=$("<span></span>");
    node_score.css("margin-left","5%")
    node_div.css("font-size","13px");
    node_div.css("color","#666");
    node_score.text("评分："+score);
    node_div.append(node_score);
    node.append(node_div);

    return node;
}

function changeWebkkitUrl(wd) {
    var stateObject = {};
    var title = wd+"-搜索结果";
    var newUrl = "/search?wd="+wd;
    history.pushState(stateObject,title,newUrl);
}
$("#search_form").bind('submit',function(){
    var wd = $("#input_search_text").val();
    changeWebkkitUrl(wd);
    search_wd();
    return false;
    });

function highlightWords(wd) {
    // wd=wd.split(" ");
    console.log(wd);
    elems=$("[result_highlight]");
    (function($){
            $('[result_highlight]').highlight(wd);
            // alert("111");

        })(jQuery)
}
function search_wd() {
   var wd = $("#input_search_text").val();
   // changeWebkkitUrl(wd);
   console.log(wd);
   $.ajax({
   type: "POST",
   url: "/search",
   data: {'wd':wd},
   success: function(msg){

     msg=JSON.parse(msg);
     data=msg['data'];
     wd_split=msg['wd_split']
      $("#search_count").text(data.length)
     console.log(data);
     rootNode=$("#search_result_tbody");
     // console.log(rootNode);
       rootNode.empty();
     for(var i=0;i<data.length;i++){
         node=createNode(data[i]);
         rootNode.append(node);
     }
      highlightWords(wd_split);
   }

});
}

