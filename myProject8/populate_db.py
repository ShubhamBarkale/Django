from blog.models import Blog

blogs = [
    {
        'title': 'Welcome to MyBlog Platform',
        'content': 'This is the first blog post on our amazing platform! We are excited to share our thoughts, ideas, and experiences with you. This platform is designed to provide a smooth and aesthetic experience for all our readers. We hope you enjoy reading our content and find it informative and engaging.\n\nStay tuned for more exciting articles coming your way!',
        'author': 'Admin'
    },
    {
        'title': 'Getting Started with Django',
        'content': 'Django is a powerful and flexible Python web framework that makes it easy to build web applications. In this article, we will explore the basics of Django and how to get started with your first project.\n\nDjango follows the Model-View-Template (MVT) architecture, which helps in organizing your code effectively. It provides built-in admin panel, ORM for database operations, and many other useful features.\n\nStart by installing Django using pip: pip install django\n\nThen create a new project and start building your applications. Django makes web development fun and productive!',
        'author': 'Django Developer'
    },
    {
        'title': 'Beautiful CSS Styling Tips',
        'content': 'CSS is the heart of web design. In this comprehensive guide, we will cover some essential tips and tricks to make your website look stunning.\n\n1. Use gradients for visual appeal\n2. Implement smooth transitions and animations\n3. Follow a consistent color scheme\n4. Use typography effectively\n5. Make your design responsive\n\nRemember that good design is not just about looks, but also about user experience. Always keep accessibility in mind when styling your web pages.',
        'author': 'Web Designer'
    },
    {
        'title': 'Best Practices in Web Development',
        'content': 'As web developers, it\'s crucial to follow best practices to write clean, maintainable, and scalable code. Here are some key principles:\n\n- Write DRY (Don\'t Repeat Yourself) code\n- Keep functions small and focused\n- Use meaningful variable and function names\n- Document your code properly\n- Write tests for your applications\n- Use version control like Git\n- Follow the project\'s coding standards\n\nBy following these practices, you\'ll become a better developer and create better applications.',
        'author': 'Senior Developer'
    },
    {
        'title': 'The Future of Web Development',
        'content': 'The web development landscape is constantly evolving. New technologies and frameworks emerge every day, making it an exciting time to be a developer.\n\nSome trends we\'re seeing:\n- More focus on performance and optimization\n- Rise of serverless architectures\n- Artificial Intelligence integration in web applications\n- Progressive Web Applications (PWAs)\n- WebAssembly for high-performance computing\n\nStay updated with the latest trends and keep learning to remain relevant in this dynamic field.',
        'author': 'Tech Analyst'
    }
]

for blog_data in blogs:
    if not Blog.objects.filter(title=blog_data['title']).exists():
        Blog.objects.create(**blog_data)
        print(f"Created: {blog_data['title']}")
    else:
        print(f"Already exists: {blog_data['title']}")

print(f"\nTotal blogs: {Blog.objects.count()}")
