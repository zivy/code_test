import SimpleITK as sitk


def sitk_write_image():
    """Repeatedly call WriteImage."""
    image = sitk.Image(300, 512, 512, sitk.sitkFloat32)
    for i in range(40):
        output = f"image-{i}.nrrd"
        print(f"Saving to {output}")
        sitk.WriteImage(image, output)


if __name__ == "__main__":
    sitk_write_image()
