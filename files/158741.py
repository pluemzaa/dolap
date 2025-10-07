<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_3"/>
        <attribute name="authors" value="spnji"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 11:38:34 PM"/>
        <attribute name="created" value="c3Buamk7TEFaWV9KSUpFRVgzOzIwMjUtMDctMjI7MTE6MzU6NDMgUE07Mjc0Mg=="/>
        <attribute name="edited" value="c3Buamk7TEFaWV9KSUpFRVgzOzIwMjUtMDctMjI7MTE6Mzg6MzQgUE07MTsyODUz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>