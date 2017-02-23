KindEditor.ready(function (K) {
    window.editor = K.create('textarea', {
        width: '550px',
        height: '400px',
        minWidth: 550,
        minHeight: 400,
        items: [
            'formatblock', 'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold',
            'italic', 'underline', 'strikethrough', 'lineheight', 'removeformat', '|', 'image', 'multiimage',
            'insertfile', 'table', 'hr', 'emoticons', 'link', 'unlink', '/',
            'undo', 'redo', '|', 'preview', 'print', '|', 'justifyleft', 'justifycenter', 'justifyright',
            'justifyfull', 'insertorderedlist', 'insertunorderedlist', 'indent', 'outdent', 'subscript',
            'superscript', 'quickformat', 'selectall', '|', 'fullscreen'],
        themeType: 'simple',
        uploadJson: '/upload_media/',
        fullscreenShortcut: true,
        extraFileUploadParams: {},
        filePostName: 'media_file',
        autoHeightMode: true,
        cssData: 'body {font-family: "宋体"; font-size: 12px}',
        fillDescAfterUploadImage: true,

    });
});
