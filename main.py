
if __name__ == '__main__':
    import click

    @click.command()

    from wqp.workflow import model_training_workflow
    model_training_workflow(data_path='http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv')
