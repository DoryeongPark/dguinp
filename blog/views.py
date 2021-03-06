from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from .models import Detail, Comment
from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm, CommentForm

def redirect_home(request):
    return redirect(' home ')

def home(request):
    return render(request, 'blog/home.html')

def htmlcss_home(request):
    posts = Detail.objects.filter(issue="htmlcss").order_by('published_date')
    return render(request, 'blog/htmlcss_home.html', {'posts' : posts})

def cpp_home(request):
    posts = Detail.objects.filter(issue="cpp").order_by('published_date')
    return render(request, 'blog/cpp_home.html', {'posts' : posts})

def java_home(request):
    posts = Detail.objects.filter(issue="java").order_by('published_date')
    return render(request, 'blog/java_home.html', {'posts' : posts})

def cs_home(request):
    posts = Detail.objects.filter(issue="cs").order_by('published_date')
    return render(request, 'blog/cs_home.html', {'posts' : posts})

def py_home(request):
    posts = Detail.objects.filter(issue="py").order_by('published_date')
    return render(request, 'blog/py_home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Detail, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Views for HTML Examples 
def background_example(request):
    return render(request, 'blog/example/background_example.html')

def image_example(request):
    return render(request, 'blog/example/image_example.html')

def frame_example1(request):
    return render(request, 'blog/example/frame_example1.html')

def frame_example2(request):
    return render(request, 'blog/example/frame_example2.html')

def frame_example3(request):
    return render(request, 'blog/example/frame_example3.html')

# View for Javascript page
def js_home(request):
    return render(request, 'blog/js_home.html')

@login_required(login_url='admin:login')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(' home ')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url='admin:login')
def post_edit(request, pk):
    post = get_object_or_404(Detail, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(' post_detail ', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Detail, pk=self.kwargs['pk'])
        comment.author = self.request.user
        comment.save()
        return super(CommentCreateView, self).form_valid(form)

comment_new = login_required(CommentCreateView.as_view())