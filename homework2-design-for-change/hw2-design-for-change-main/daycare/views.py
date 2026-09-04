from django.shortcuts import get_object_or_404, redirect, render

from .models import Dragon


def home(request):
    puff, _ = Dragon.objects.get_or_create(name="Puff")

    # Presentation logic and care policy are intentionally mixed here.
    if puff.hunger >= 8:
        banner = "URGENT: Puff needs food now."
    elif puff.hunger >= 6:
        banner = "Puff may need a snack soon."
    elif puff.energy <= 2:
        banner = "Puff needs rest."
    else:
        banner = "Puff is doing fine."

    return render(
        request,
        "daycare/home.html",
        {
            "puff": puff,
            "banner": banner,
            "status": puff.status_message(),
        },
    )


def feed_puff(request, dragon_id):
    puff = get_object_or_404(Dragon, id=dragon_id)
    if request.method == "POST":
        puff.feed()
        puff.save()
    return redirect("home")
