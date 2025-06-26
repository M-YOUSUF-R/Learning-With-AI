const quill = new Quill('.editor', {
    modules: {
    toolbar: '#toolbar',
    // toolbar: [
    //     [{ header: [1, 2, false] }],
    //     ['bold', 'italic', 'underline'],
    //     ['image', 'code-block'],
    //     [{ 'list': 'ordered'}, { 'list': 'bullet' }, { 'list': 'check' }],
    //   ],
    },
    theme: 'snow'
});

export default quill