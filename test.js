function enableImageOverlay() {
    var text = document.getElementById("is_text")
    text.style.backgroundColor = "#0066ff"
    text.style.color = "white"
    text.style.fontSize = "16px"
    text.style.padding = "16px 32px"
    text.style.cursor = "pointer"

    var profileImage = document.getElementById("id_profile_image")
    profileImage.style.opacity = "1"
    profileImage.style.display = "block"
    profileImage.style.width = "100%"
    profileImage.style.height = "auto"
    profileImage.style.transition = ".5s ease"
    profileImage.style.backfaceVisibility = "hidden"
    profileImage.style.cursor = 'pointer'

    var middleContainer = document.getElementById("id_middle_container")
    middleContainer.style.transition = ".5s ease"
    middleContainer.style.opacity = "0"
    middleContainer.style.position = "absolute"
    middleContainer.style.top = "50%"
    middleContainer.style.left = "50%"
    middleContainer.style.transition = "translate(-50%, -50%)"
}