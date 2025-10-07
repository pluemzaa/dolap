<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_4"/>
        <attribute name="authors" value="teera"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-18 11:25:20 PM"/>
        <attribute name="created" value="dGVlcmE7REVTS1RPUC1UMFBBVTZIOzI1NjgtMDctMTg7MTE6MDA6NDcgUE07Mjg5NA=="/>
        <attribute name="edited" value="dGVlcmE7REVTS1RPUC1UMFBBVTZIOzI1NjgtMDctMTg7MTE6MjU6MjAgUE07NjszMDA1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Money" type="Real" array="False" size=""/>
            <declare name="Year, i, interest" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="Money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="Year"/>
            <while expression="i&lt;Year">
                <assign variable="Money" expression="Money*(interest/100+(1))"/>
                <output expression="&quot; Year &quot;&amp;i + 1&amp; &quot;: &quot;&amp;Money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>