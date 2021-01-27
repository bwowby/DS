{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNC21Si0Vu5XiXD2/+DSZrS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bwowby/DS/blob/master/basic-nlp/bow.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8_YnPF_wbj6o"
      },
      "source": [
        "## BOW : Bag of Words\r\n",
        "\r\n",
        "*  가장 간단하지만, 자연어 처리에서 널리 쓰이는 개념적 방법.\r\n",
        "*  각 단어가 말뭉치(corpus)에 얼마나 많이 나타나는지만 헤아림.\r\n",
        "*  구조와 상관없이 단어의 출현 횟수만 카운팅.   \r\n",
        "*  횟수가 중요하기 때문에 단어의 순서가 달라도 같은 반환값을 가짐.\r\n",
        "*  이를 보완하기 위해 n-gram (n개의 토큰) 사용\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "\r\n",
        "   \r\n",
        "\r\n",
        "\r\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WkTRPOr3cZot"
      },
      "source": [
        "### 예제"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HXlUH4XAZ48G"
      },
      "source": [
        "#사이킷런의 CountVectorizer를 통해 벡터화\r\n",
        "from sklearn.feature_extraction.text import CountVectorizer"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "C4cHiQYodsH6"
      },
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CXww5CQYbcdo",
        "outputId": "b7aaf7cf-639c-4f1e-85f2-c20a01457470"
      },
      "source": [
        "vectorizer = CountVectorizer(analyzer = 'word', #캐릭터 단위로도 벡터화 가능\r\n",
        "                             tokenizer = None,\r\n",
        "                             preprocessor = None, #전처리 도구\r\n",
        "                             stop_words = None, #\r\n",
        "                             min_df = 1, #토큰이 나타날 최소 문서 갯수\r\n",
        "                             ngram_range = (1,1))\r\n",
        "vectorizer"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "CountVectorizer(analyzer='word', binary=False, decode_error='strict',\n",
              "                dtype=<class 'numpy.int64'>, encoding='utf-8', input='content',\n",
              "                lowercase=True, max_df=1.0, max_features=None, min_df=1,\n",
              "                ngram_range=(1, 1), preprocessor=None, stop_words=None,\n",
              "                strip_accents=None, token_pattern='(?u)\\\\b\\\\w\\\\w+\\\\b',\n",
              "                tokenizer=None, vocabulary=None)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yBLHmoIfd5w6"
      },
      "source": [
        "\r\n",
        "corpus = ['The proposed rising was a dismal failure, but the Habeas Corpus Act was suspended and Thistlewood and Watson were seized, although upon being tried they were acquitted.', \r\n",
        "         'Before the prorogation, however, he saw the invaluable Act of Habeas Corpus, which he had carried through parliament, receive the royal assent.', \r\n",
        "         'These Personal Liberty Laws forbade justices and judges to take cognizance of claims, extended the habeas corpus act and the privilege of jury trial to fugitives, and punished false testimony severely.', \r\n",
        "         'The procession of the Host on Corpus Christi day became, as it were, a public demonstration of Catholic orthodoxy against Protestantism and later against religious Liberalism.']\r\n",
        "#출처: https://hong-yp-ml-records.tistory.com/34 [HONG YP's Data Science BLOG]\r\n",
        "#https://sentence.yourdictionary.com/corpus"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L7hUU41ZecJs",
        "outputId": "77d6bfb8-8470-43d7-fd1c-a60cd6c21798"
      },
      "source": [
        "#단어를 기준으로 한 featrue 만들기 -> sparse한 array 형태로 만들어짐\r\n",
        "features = vectorizer.fit_transform(corpus)\r\n",
        "print(features)"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "  (0, 61)\t2\n",
            "  (0, 46)\t1\n",
            "  (0, 53)\t1\n",
            "  (0, 70)\t2\n",
            "  (0, 19)\t1\n",
            "  (0, 21)\t1\n",
            "  (0, 10)\t1\n",
            "  (0, 25)\t1\n",
            "  (0, 16)\t1\n",
            "  (0, 1)\t1\n",
            "  (0, 58)\t1\n",
            "  (0, 4)\t2\n",
            "  (0, 64)\t1\n",
            "  (0, 71)\t1\n",
            "  (0, 72)\t2\n",
            "  (0, 56)\t1\n",
            "  (0, 3)\t1\n",
            "  (0, 69)\t1\n",
            "  (0, 9)\t1\n",
            "  (0, 68)\t1\n",
            "  (0, 63)\t1\n",
            "  (0, 0)\t1\n",
            "  (1, 61)\t3\n",
            "  (1, 25)\t1\n",
            "  (1, 16)\t1\n",
            "  :\t:\n",
            "  (2, 22)\t1\n",
            "  (2, 60)\t1\n",
            "  (2, 57)\t1\n",
            "  (3, 61)\t2\n",
            "  (3, 16)\t1\n",
            "  (3, 4)\t1\n",
            "  (3, 72)\t1\n",
            "  (3, 39)\t2\n",
            "  (3, 45)\t1\n",
            "  (3, 28)\t1\n",
            "  (3, 40)\t1\n",
            "  (3, 13)\t1\n",
            "  (3, 17)\t1\n",
            "  (3, 7)\t1\n",
            "  (3, 5)\t1\n",
            "  (3, 31)\t1\n",
            "  (3, 49)\t1\n",
            "  (3, 18)\t1\n",
            "  (3, 12)\t1\n",
            "  (3, 41)\t1\n",
            "  (3, 2)\t2\n",
            "  (3, 48)\t1\n",
            "  (3, 35)\t1\n",
            "  (3, 52)\t1\n",
            "  (3, 37)\t1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E5v_EdUee1Co",
        "outputId": "454ee265-b97b-4260-dffc-2d553d263f16"
      },
      "source": [
        "#4개의 관측치, 74개의 단어로 이루어짐\r\n",
        "features.shape"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4, 74)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5EgSd45nfNv7",
        "outputId": "4513bf0e-e373-4084-ee04-ef20a447ac38"
      },
      "source": [
        "vocab = vectorizer.get_feature_names()\r\n",
        "print(len(vocab))\r\n",
        "vocab[:10]"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "74\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['acquitted',\n",
              " 'act',\n",
              " 'against',\n",
              " 'although',\n",
              " 'and',\n",
              " 'as',\n",
              " 'assent',\n",
              " 'became',\n",
              " 'before',\n",
              " 'being']"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "j_8D3UJtfqO4"
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 193
        },
        "id": "Be9kaL81f2ov",
        "outputId": "5828e599-731a-46f7-bc67-24656ad2c8d2"
      },
      "source": [
        "pd.DataFrame(features.toarray(), columns = vocab).head()"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>acquitted</th>\n",
              "      <th>act</th>\n",
              "      <th>against</th>\n",
              "      <th>although</th>\n",
              "      <th>and</th>\n",
              "      <th>as</th>\n",
              "      <th>assent</th>\n",
              "      <th>became</th>\n",
              "      <th>before</th>\n",
              "      <th>being</th>\n",
              "      <th>but</th>\n",
              "      <th>carried</th>\n",
              "      <th>catholic</th>\n",
              "      <th>christi</th>\n",
              "      <th>claims</th>\n",
              "      <th>cognizance</th>\n",
              "      <th>corpus</th>\n",
              "      <th>day</th>\n",
              "      <th>demonstration</th>\n",
              "      <th>dismal</th>\n",
              "      <th>extended</th>\n",
              "      <th>failure</th>\n",
              "      <th>false</th>\n",
              "      <th>forbade</th>\n",
              "      <th>fugitives</th>\n",
              "      <th>habeas</th>\n",
              "      <th>had</th>\n",
              "      <th>he</th>\n",
              "      <th>host</th>\n",
              "      <th>however</th>\n",
              "      <th>invaluable</th>\n",
              "      <th>it</th>\n",
              "      <th>judges</th>\n",
              "      <th>jury</th>\n",
              "      <th>justices</th>\n",
              "      <th>later</th>\n",
              "      <th>laws</th>\n",
              "      <th>liberalism</th>\n",
              "      <th>liberty</th>\n",
              "      <th>of</th>\n",
              "      <th>on</th>\n",
              "      <th>orthodoxy</th>\n",
              "      <th>parliament</th>\n",
              "      <th>personal</th>\n",
              "      <th>privilege</th>\n",
              "      <th>procession</th>\n",
              "      <th>proposed</th>\n",
              "      <th>prorogation</th>\n",
              "      <th>protestantism</th>\n",
              "      <th>public</th>\n",
              "      <th>punished</th>\n",
              "      <th>receive</th>\n",
              "      <th>religious</th>\n",
              "      <th>rising</th>\n",
              "      <th>royal</th>\n",
              "      <th>saw</th>\n",
              "      <th>seized</th>\n",
              "      <th>severely</th>\n",
              "      <th>suspended</th>\n",
              "      <th>take</th>\n",
              "      <th>testimony</th>\n",
              "      <th>the</th>\n",
              "      <th>these</th>\n",
              "      <th>they</th>\n",
              "      <th>thistlewood</th>\n",
              "      <th>through</th>\n",
              "      <th>to</th>\n",
              "      <th>trial</th>\n",
              "      <th>tried</th>\n",
              "      <th>upon</th>\n",
              "      <th>was</th>\n",
              "      <th>watson</th>\n",
              "      <th>were</th>\n",
              "      <th>which</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   acquitted  act  against  although  and  ...  upon  was  watson  were  which\n",
              "0          1    1        0         1    2  ...     1    2       1     2      0\n",
              "1          0    1        0         0    0  ...     0    0       0     0      1\n",
              "2          0    1        0         0    3  ...     0    0       0     0      0\n",
              "3          0    0        2         0    1  ...     0    0       0     1      0\n",
              "\n",
              "[4 rows x 74 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C4DA-563f8eL"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}