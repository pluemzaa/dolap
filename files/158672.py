<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="interest"/>
        <attribute name="authors" value="prera"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 05:02:14 PM"/>
        <attribute name="created" value="cHJlcmE7UFJPR1JBTTsyNTY4LTA3LTIyOzEyOjM3OjE2IFBNOzIzNzA="/>
        <attribute name="edited" value="cHJlcmE7UFJPR1JBTTsyNTY4LTA3LTIyOzA1OjAyOjE0IFBNOzM7MjQ3Mg=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="in, year, i, n, y" type="Integer" array="False" size=""/>
            <declare name="ins, total, mouths" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="mouths"/>
            <output expression="&quot;In put interest(%):&quot;" newline="True"/>
            <input variable="in"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <assign variable="N" expression="0"/>
            <assign variable="total" expression="0"/>
            <while expression="i&lt;year">
                <assign variable="mouths" expression="mouths*(1+in*0.01)"/>
                <assign variable="i" expression="i+1"/>
                <output expression="&quot;Year &quot;&amp;i&amp;&quot;: &quot;&amp;mouths" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>