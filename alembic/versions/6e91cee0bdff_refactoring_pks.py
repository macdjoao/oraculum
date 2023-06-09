"""refactoring pks

Revision ID: 6e91cee0bdff
Revises:
Create Date: 2023-06-07 23:08:34.551298
"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '6e91cee0bdff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'grades',
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('name'),
    )
    op.create_table(
        'races',
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('name'),
    )
    op.create_table(
        'players',
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.Integer(), nullable=True),
        sa.Column('race', sa.String(), nullable=True),
        sa.Column('grade', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ['grade'],
            ['grades.name'],
        ),
        sa.ForeignKeyConstraint(
            ['race'],
            ['races.name'],
        ),
        sa.PrimaryKeyConstraint('name'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players')
    op.drop_table('races')
    op.drop_table('grades')
    # ### end Alembic commands ###
