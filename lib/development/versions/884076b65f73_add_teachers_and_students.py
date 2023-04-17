"""add teachers and students

Revision ID: 884076b65f73
Revises: 52f3e9b380b1
Create Date: 2023-04-17 15:23:28.814423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '884076b65f73'
down_revision = '52f3e9b380b1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    op.drop_table('students')
    # ### end Alembic commands ###
